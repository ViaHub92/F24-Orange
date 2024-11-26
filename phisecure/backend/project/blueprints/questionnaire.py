from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from backend.project import db
from database.models.questionnaire import Questionnaire, Question, Response, Answer, Option
from database.models.student import Student
from database.models.template import StudentProfile
from backend.project.routes import routes
from marshmallow import Schema, fields, ValidationError
from database.schemas.response_schema import ResponseSchema
from flask import current_app


questionnaire = Blueprint('questionnaire', __name__)

# Route for the Questionnaire
@questionnaire.route("", methods=["POST"])
def create_questionnaire():
    """ 
    Route for creating a new questionnaire with no questions
    """
    if request.method == "POST":
       data = request.get_json()
       name = data.get('name')
       description = data.get('description')
    existing_questionnaire = Questionnaire.query.filter_by(name=name).first()
    if existing_questionnaire:
        return jsonify({"error": "Questionnaire with this name already exists"}), 400
    else:
        new_questionnaire = Questionnaire(name=name, description=description)
        # loop to iterate through the questions in the questionnaire
        for question in data.get('questions'):
            question_text = question.get('question_text') # get the question text
            question_type = question.get('question_type') # get the question type
            new_question = Question(
                questionnaire=new_questionnaire, 
                question_text=question_text, 
                question_type=question_type
            )
            if question_type in ["true/false", "multiple choice", "yes/no"]: #checks question type
                for option in question.get('options'): # loop to iterate through the options for the question
                    option_text = option.get('option_text')
                    new_option = Option(question=new_question, option_text=option_text)
                    db.session.add(new_option)
                    
        db.session.add(new_question)
        db.session.add(new_questionnaire)
        db.session.commit()
        return jsonify(new_questionnaire.serialize()), 200

@questionnaire.route("/<questionnaire_id>", methods=["GET"])
def get_questionnaire(questionnaire_id):
    """
    Route for retrieving a specific questionnaire
    """
    if request.method == "GET":
        found_questionnaire = Questionnaire.query.get(questionnaire_id)
        if not found_questionnaire:
            return jsonify({"error": "Questionnaire not found"}), 404
        return jsonify(found_questionnaire.serialize()), 200

@questionnaire.route("/<questionnaire_id>", methods=["PUT"])
def update_questionnaire(questionnaire_id):
    """  backend endpoint for updating a questionnaire
    Args:
        questionnaire_id (_type_): unique identifier for the questionnaire.

    Returns:
    
        _type_: newly updated questionnaire
    """
    if request.method == "PUT":
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')

        # Fetch the questionnaire to update
        questionnaire = Questionnaire.query.get(questionnaire_id)
        if not questionnaire:
            return jsonify({"error": "Questionnaire not found"}), 404

        # Update questionnaire's basic details
        if name:
            # Check for duplicate name
            existing_questionnaire = Questionnaire.query.filter_by(name=name).first()
            if existing_questionnaire and existing_questionnaire.id != questionnaire_id:
                return jsonify({"error": "Another questionnaire with this name already exists"}), 400
            questionnaire.name = name
        
        if description:
            questionnaire.description = description

        # Update or add questions
        for question_data in data.get('questions', []):
            question_id = question_data.get('id')  # Existing question ID (if updating)
            question_text = question_data.get('question_text')
            question_type = question_data.get('question_type')

            if question_id:
                # Update existing question
                question = Question.query.get(question_id)
                if question:
                    question.question_text = question_text or question.question_text
                    question.question_type = question_type or question.question_type

                    # Update options for existing question
                    if question_type in ["true/false", "multiple choice", "yes/no"]:
                        for option_data in question_data.get('options', []):
                            option_id = option_data.get('id')
                            option_text = option_data.get('option_text')

                            if option_id:
                                # Update existing option
                                option = Option.query.get(option_id)
                                if option:
                                    option.option_text = option_text
                            else:
                                # Add a new option to the existing question
                                new_option = Option(question=question, option_text=option_text)
                                db.session.add(new_option)
                else:
                    return jsonify({"error": f"Question with ID {question_id} not found"}), 404
            else:
                # Add new question
                new_question = Question(
                    questionnaire=questionnaire, 
                    question_text=question_text, 
                    question_type=question_type
                )

                # Add options for the new question
                if question_type in ["true/false", "multiple choice", "yes/no"]:
                    for option in question_data.get('options', []):
                        option_text = option.get('option_text')
                        new_option = Option(question=new_question, option_text=option_text)
                        db.session.add(new_option)

                db.session.add(new_question)

        try:
            # Save changes to the database
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": f"Failed to update questionnaire: {str(e)}"}), 500

        return jsonify(questionnaire.serialize()), 200
    
@questionnaire.route("/Submit/<int:student_id>", methods=["POST"])
def submit_response(student_id):
    """
    Route for submitting a response to a questionnaire
    """
    if request.method == "POST":
        data = request.get_json()
        
        #Validate the data
        schema = ResponseSchema()
        try:
            validated_data = schema.load(data) # This will raise a ValidationError if the data is invalid
        except ValidationError as err:
            print("Validation error", err.messages)
            return jsonify(err.messages), 400 # Return the validation error messages
        
          # Check if the student_id exists
        student = Student.query.get(student_id)
        if not student:
            print(f"Student ID {student_id} does not exist")
            return jsonify({"error": "Student ID does not exist"}), 400
        
        #Create a student profile with default values if it does not exist
        student_profile = StudentProfile.query.filter_by(student_id=student_id).first()
        if not student_profile:
            student_profile = StudentProfile(
                student_id=student_id,
                first_name=student.first_name,
                major="Undeclared",
                email_used_for_platforms=student.email,
                employement_status="Unemployed",
                employer=None,
                risk_level="Low",
                attention_to_detail="High"
            )
            db.session.add(student_profile) 
            
            try:
                db.session.commit()  
                print(f"Created student profile with ID: {student_profile.id}")
            except Exception as e:
                print(f"Error creating student profile: {str(e)}")
                db.session.rollback()
                return jsonify({"error": "Failed to create student profile"}), 500
        else:
            print(f"Found existing student profile with ID: {student_profile.id}")
            
        #If the data is valid, create the response
        questionnaire_id = validated_data['questionnaire_id']
        #check if a response has already been submitted for this questionnaire by this student
        existing_response = Response.query.filter_by(student_id=student_id, questionnaire_id=questionnaire_id).first()
        
        if existing_response:
            return jsonify({"error": "A response for this questionnaire already exists for this student."}), 400
        
        answers = validated_data['answers']
        
        #Create a new response
        new_response = Response(questionnaire_id=questionnaire_id, 
                                student_id=student_id, 
                                student_profile_id=student_profile.id) 
        for answer in answers: # loop to iterate through the answers
            question_id = answer.get('question_id') # get the question id
            answer_text = answer.get('answer_text') # get the answer text
            new_answer = Answer(
                response=new_response, 
                question_id=question_id, 
                answer_text=answer_text
            )
            db.session.add(new_answer)
        db.session.add(new_response)
       
        
        #Update the student profile employment status and employer information based on answers given.
        student_profile.update_attributes_from_answers(questionnaire_id)
        
        #Assign tags to the student profile based on the answers given
        try:
            student_profile.assign_tags_to_profiles(questionnaire_id)
            assigned_tags = student_profile.get_assigned_tags_from_student_profile()
            
            if not assigned_tags:
                raise Exception("No tags assigned")
        except Exception as e:
            print(f"Error assigning tags: {str(e)}")
            db.session.rollback()
            return jsonify({"error": "Failed to assign tags"}), 500
        
        db.session.commit()
        
        for i in range(5):
            try:
                # Prepare the data for the phishing email
                phishing_email_data = {
                    'recipient_id': student_id  # Assuming you want to send to the same student
                }
                
                # Call the phishing email endpoint using Flask test client
                with current_app.test_client() as client:
                    response = client.post('/messaging/compose_phishing_email', json=phishing_email_data)
                    
                    if response.status_code != 201:
                        print(f"Failed to send phishing email: {response.json.get('error')}")
            except Exception as e:
                print(f"Error calling phishing email endpoint: {str(e)}")
                db.session.rollback()
                return jsonify({"error": "Failed to call phishing email endpoint"}), 500
        
        
        return jsonify(new_response.serialize()), 200
    
@questionnaire.route("/questions/<question_id>", methods=["PUT"])
def update_question(question_id):
    """
    Route for updating a question in a questionnaire
    """
    if request.method == "PUT":
        data = request.get_json()
        question_text = data.get('question_text')
        question_type = data.get('question_type')
        question = Question.query.get(question_id)
        if not question:
            return jsonify({"error": "Question not found"}), 404
        question.question_text = question_text
        question.question_type = question_type
        if question_type in ["true/false", "multiple choice", "yes/no"]:
            #Clear existing options if any
            Option.query.filter_by(question_id=question_id).delete()
            
            for option in data.get('options'): # loop to iterate through the options
                option_text = option.get('option_text')
                new_option = Option(question=question, option_text=option_text)
                db.session.add(new_option)
        
        db.session.commit()
        return jsonify(question.serialize()), 200
    

@questionnaire.route("/response/<response_id>", methods=["GET"])
def get_response(response_id):
    """
    Route for retrieving a specific response
    """
    if request.method == "GET":
        found_response = Response.query.get(response_id)
        if not found_response:
            return jsonify({"error": "Response not found"}), 404
        return jsonify(found_response.serialize()), 200      
       
    
