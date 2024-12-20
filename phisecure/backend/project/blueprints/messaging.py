from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from backend.project import db
from database.models.student import Student
from database.models.email import Email
from database.models.phishing_email import PhishingEmail
from database.models.inbox import Inbox
from database.models.user_interaction import UserInteraction
from database.models.template import Template, StudentProfile, TemplateTag, Tag
from datetime import datetime, timezone
from backend.project.routes import routes

messaging = Blueprint('messaging', __name__, template_folder='templates')

# Route for the inbox
@messaging.route('/inbox/<int:student_id>')
def inbox(student_id):
    """
    Route to retrieve the inbox for a specific student.
    """
    if not student_id:
        flash('Student ID is required.')
        return redirect(url_for('routes.index'))

    # Find the student by ID
    student = Student.query.get(student_id)
    if not student:
        flash('Student not found.')
        return redirect(url_for('routes.index'))
    
    # Get all normal emails sent to this student
    inbox_emails = Email.query.filter_by(recipient=student.email).all()
    
    # Get all phishing emails sent to this student
    inbox_phishing_emails = PhishingEmail.query.filter_by(recipient=student.email).all()

    # Initialize email_list as an empty list
    email_list = []

    # Convert normal emails to a serializable format
    for email in inbox_emails:
        email_list.append({
            "id": email.id,
            "sender": email.sender,
            "recipient": email.recipient,
            "subject": email.subject,
            "body": email.body,
            "sent_at": email.sent_at
        })

    # Convert phishing emails to a serializable format
    for phishing_email in inbox_phishing_emails:
        email_list.append({
            "id": phishing_email.id,
            "sender": phishing_email.sender,
            "recipient": phishing_email.recipient,
            "subject": phishing_email.subject,
            "body": phishing_email.body,
            "sent_at": phishing_email.sent_at
        })

    email_list.sort(key=lambda x: x['sent_at'], reverse=True)

    # Convert datetime to ISO format for the response
    for email in email_list:
        email['sent_at'] = email['sent_at'].isoformat()
    
    return jsonify({"inbox": email_list}), 200


@messaging.route('/compose_email', methods=['POST'])
def compose_email():
    """
    Route to send a normal email to a recipient.
    """
    recipient_email = request.form.get('recipient')
    
    # Check if the recipient is valid
    recipient_student = Student.query.filter_by(email=recipient_email).first()
    if not recipient_student:
        flash('Recipient does not exist.')
        return redirect(url_for('messaging.compose_email'))

    # For normal emails, use provided subject and body
    subject = request.form.get('subject')
    body = request.form.get('body')

    # Ensure subject and body are provided for normal emails
    if not subject or not body:
        flash('Subject and body are required for normal emails.')
        return redirect(url_for('messaging.compose_email'))

    # Create a regular email
    email = Email(
        sender=request.form.get('sender'),
        recipient=recipient_email,
        subject=subject,
        body=body,
        sent_at=datetime.now(timezone.utc),
        inbox_id=recipient_student.inbox_id
    )
    db.session.add(email)
    db.session.commit()
    
    flash('Normal email sent successfully!')
    return redirect(url_for('messaging.inbox', student_id=recipient_student.id))


@messaging.route('/compose_phishing_email/<int:student_id>', methods=['POST'])
def compose_phishing_email(student_id):
    """
    Compose a phishing email by finding a matching template based on recipient tags
    and populating the template with recipient data. If no matching template is found,
    a "generic" template will be used instead.
    """

    recipient = Student.query.get(student_id)
    if not recipient:
        return jsonify({'error': 'Recipient not found'}), 404

    profile = StudentProfile.query.filter_by(student_id=recipient.id).first()
    if not profile:
        return jsonify({'error': 'Recipient profile not found'}), 404

    recipient_tags = {tag.name for tag in profile.tags}

    if not recipient_tags:
        return jsonify({'error': 'Recipient has no associated tags'}), 400

    matching_templates = (
        Template.query.join(Template.tags)
        .filter(Tag.name.in_(recipient_tags))
        .distinct()
        .all()
    )

    sent_templates = PhishingEmail.query.filter_by(inbox_id=recipient.inbox_id).all()
    sent_template_ids = {email.template_id for email in sent_templates}
    
    available_template = None
    for template in matching_templates:
        if template.id not in sent_template_ids:
            available_template = template
            break

    if not available_template:
        generic_templates = Template.query.join(Template.tags).filter(Tag.name == "generic").all()
        for generic_template in generic_templates:
            if generic_template.id not in sent_template_ids:
                available_template = generic_template
                break
            
    if not available_template:
            return jsonify({'error': 'No templates left to send to this student'}), 404

    template = available_template

    link = template.link
    if '{link}' in template.body_template and not link:
        return jsonify({'error': 'Template requires a link, but none was provided.'}), 400

    try:
        body = template.body_template.format(
            first_name=recipient.first_name,
            employer=profile.employer,
            company_name=profile.employer,
            link=link if '{link}' in template.body_template else "",
            date=datetime.now().strftime("%B %d, %Y")
        ).replace('\n', '<br>')
        subject = template.subject_template.format(first_name=recipient.first_name)
    except KeyError as e:
        return jsonify({'error': f'Missing placeholder in recipient data: {e}'}), 400

    phishing_email = PhishingEmail(
        sender=template.sender_template,
        recipient=recipient.email,
        subject=subject,
        body=body,
        sent_at=datetime.now(timezone.utc),
        inbox_id=recipient.inbox_id,
        red_flag=template.template_redflag,
        template_id=template.id
    )
    db.session.add(phishing_email)

    interaction = UserInteraction(
        student_id=recipient.id,
        phishing_email=phishing_email,
        opened=False,
        link_clicked=False,
        replied=False
    )
    db.session.add(interaction)

    db.session.commit()

    return jsonify({
        'template_id': template.id,
        'recipient': recipient.email,
        'subject': subject,
        'body': body,
        'sent_at': phishing_email.sent_at.isoformat()
    }), 201

@messaging.route('/view/<email_id>', methods=['GET'])
def view_email(email_id):
    """
    Route to view a specific email (normal or phishing).
    """
    # Attempt to find the email by its ID in both Email and PhishingEmail tables
    email = Email.query.get(email_id)
    is_phishing = False

    # If not found in regular Email, check PhishingEmail table
    if not email:
        email = PhishingEmail.query.get(email_id)
        is_phishing = True
    
    if not email:
        flash('Email not found.')
        return redirect(url_for('messaging.inbox'))

    # If the email is a phishing email, update interaction if exists
    student_id = request.args.get('student_id')
    if is_phishing and student_id:
        interaction = UserInteraction.query.filter_by(student_id=student_id, phishing_email_id=email_id).first()
        if interaction:
            print("it is a phishing email")
            interaction.opened = True
            db.session.commit()

    # Render the email view template or return JSON data
    return jsonify({
        "email_id": email.id,
        "sender": email.sender,
        "recipient": email.recipient,
        "subject": email.subject,
        "body": email.body,
        "is_phishing": is_phishing
    }), 200


# Route to handle replying to an email
@messaging.route('/reply/<email_id>', methods=['POST'])
def reply_email(email_id):
    """
    Route to reply to a specific email.
    """
    # Check both Email and PhishingEmail for the email
    email = Email.query.get(email_id)
    is_phishing = False

    if not email:
        email = PhishingEmail.query.get(email_id)
        is_phishing = True

    if not email:
        flash('Email not found.')
        return redirect(url_for('messaging.inbox'))

    # Get reply message from the form
    data = request.get_json()
    reply_body = data.get('reply_body')
    
    student_id = request.args.get('student_id')
    if not student_id:
        flash("Student ID is missing")
        return redirect(url_for('messaging.inbox'))

    # Only update interaction if this is a phishing email
    if is_phishing:
        interaction = UserInteraction.query.filter_by(student_id=student_id, phishing_email_id=email_id).first()
        if interaction:
            interaction.replied = True
            db.session.commit()
        else:
            flash('No interaction found for this email.')
    
    flash('Reply sent successfully!')
    return redirect(url_for('messaging.inbox', student_id=student_id))

# Route to handle deleting an email
@messaging.route('/delete/<email_id>', methods=['POST'])
def delete_email(email_id):
    """
    Route to delete a specific email (normal or phishing).
    """
    # Attempt to find the email in both Email and PhishingEmail tables
    email = Email.query.get(email_id)
    phishing_email = PhishingEmail.query.get(email_id)

    # Check if the email was found in either table
    if email:
        # Delete the regular email
        db.session.delete(email)
    elif phishing_email:
        # Delete the phishing email
        db.session.delete(phishing_email)
    else:
        flash('Email not found.')
        return redirect(url_for('messaging.inbox'))  # Redirect back to inbox if email not found

    # Commit the deletion to the database
    db.session.commit()
    
    flash('Email deleted successfully!')
    return redirect(url_for('messaging.inbox'))  # Redirect back to inbox

# Route to handle tracking link clicks for phishing emails
@messaging.route('/track/<email_id>', methods=['POST'])
def track_link(email_id):
    """
    Track when a phishing email link is clicked.
    """

    student_id = request.args.get('student_id')  
    if not student_id:
        
        return jsonify({'error': 'Student ID is missing'}), 400   
    
    interaction = UserInteraction.query.filter_by(
        phishing_email_id=email_id, student_id=student_id
    ).first()

    if not interaction:
        return jsonify({'error': 'Interaction record not found'}), 404

    if not interaction.link_clicked:
        interaction.link_clicked = True
        db.session.commit()

    return jsonify({'message': 'Interaction recorded'}), 200


