from flask import Blueprint, render_template, redirect, url_for, request, flash
from project import db
from project.models import User, Email, Inbox
from datetime import datetime, timezone
from project.routes import routes


messaging = Blueprint('messaging', __name__, template_folder='templates')

# Route for the inbox
@messaging.route('/inbox')
def inbox():
    user_id = request.args.get('user_id')
    if not user_id:
        flash('User ID is required.')
        return redirect(url_for('routes.index'))

    # Find the user by ID
    user = User.query.get(user_id)
    if not user:
        flash('User not found.')
        return redirect(url_for('routes.index'))

    # Get all emails sent to this user
    inbox_emails = Email.query.filter_by(recipient=user.email).all()
    return render_template('inbox.html', emails=inbox_emails)

# Route for composing a message
@messaging.route('/compose', methods=['GET', 'POST'])
def compose():
    if request.method == 'POST':
        sender_email = request.form.get('sender')  # sender email is now passed from form
        recipient_email = request.form.get('recipient')
        subject = request.form.get('subject')
        body = request.form.get('body')

        # Check if the recipient is valid
        recipient_user = User.query.filter_by(email=recipient_email).first()
        if not recipient_user:
            flash('Recipient does not exist.')
            return redirect(url_for('messaging.compose'))

        # Create the new email and save it
        email = Email(
            sender=sender_email,
            recipient=recipient_email,
            subject=subject,
            body=body,
            sent_at=datetime.now(timezone.utc),
            inboxs=recipient_user.inbox_id  # Link the email to recipient's inbox
        )

        db.session.add(email)
        db.session.commit()
        flash('Message sent successfully!')
        return redirect(url_for('messaging.inbox', user_id=recipient_user.id))

    return render_template('compose.html')
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
