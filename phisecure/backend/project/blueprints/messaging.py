from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from backend.project import db
from database.models.student import Student  # Import Student model instead of User
from database.models.email import Email
from database.models.inbox import Inbox
from datetime import datetime, timezone
from backend.project.routes import routes

messaging = Blueprint('messaging', __name__, template_folder='templates')

# Route for the inbox
@messaging.route('/inbox')
def inbox():
    student_id = request.args.get('student_id')
    if not student_id:
        flash('Student ID is required.')
        return redirect(url_for('routes.index'))

    # Find the student by ID
    student = Student.query.get(student_id)
    if not student:
        flash('Student not found.')
        return redirect(url_for('routes.index'))
    
    # Get all emails sent to this student
    inbox_emails = Email.query.filter_by(recipient=student.email).all()

    # Initialize email_list as an empty list
    email_list = []

    # Convert emails to a serializable format
    for email in inbox_emails:
        email_list.append({
            "id": email.id,
            "sender": email.sender,
            "recipient": email.recipient,
            "subject": email.subject,
            "body": email.body,
            "sent_at": email.sent_at.isoformat()  # Convert datetime to ISO format
        })
    return jsonify({"inbox": email_list}), 200

# Route for composing a message
@messaging.route('/compose', methods=['GET', 'POST'])
def compose():
    if request.method == 'POST':
        sender_email = request.form.get('sender')  # sender email is now passed from form
        recipient_email = request.form.get('recipient')
        subject = request.form.get('subject')
        body = request.form.get('body')

        # Check if the recipient is valid
        recipient_student = Student.query.filter_by(email=recipient_email).first()
        if not recipient_student:
            flash('Recipient does not exist.')
            return redirect(url_for('messaging.compose'))

        # Create the new email and save it
        email = Email(
            sender=sender_email,
            recipient=recipient_email,
            subject=subject,
            body=body,
            sent_at=datetime.now(timezone.utc),
            inboxs=recipient_student.inbox_id  # Link the email to recipient's inbox
        )

        db.session.add(email)
        db.session.commit()
        flash('Message sent successfully!')
        return redirect(url_for('messaging.inbox', user_id=recipient_student.id))

    return jsonify({"message": "Compose message form displayed."}), 200

# Route to view a specific email
@messaging.route('/view/<int:email_id>')
def view_email(email_id):
    email = Email.query.get(email_id)
    if not email:
        flash('Email not found.')
        return redirect(url_for('messaging.inbox'))

    # Mark email as read
    email.is_read = True
    db.session.commit()
    
    return render_template('view_email.html', email=email)
