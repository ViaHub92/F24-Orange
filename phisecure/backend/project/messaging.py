"""
messaging.py
Team Orange
Last Modified: 9/12/24
Purpose: Contains logic for messaging between accounts and their email environments
"""

from project import db
from project.models import User, Email, Inbox  # Import models from Flask app
from datetime import datetime, timezone

# Function to check the account's email
def check_email(acc): 
    inbox = Inbox.query.get(acc.inbox_id)
    print(inbox)
    return

# Function to check the account for unread emails
def check_for_unread_emails(acc):
    inbox = Inbox.query.get(acc.inbox_id)
    results = inbox.query.get(is_read=False)
    print(results)
    return

# Function to send an email to a given account
def send_email(email, acc):
    return

# Function to manage the current user's account
def manage_account(acc):
    """
    Function that manages the given account
    :param acc: The current user's account
    :returns: N/A
    """
    user_input = ""
    
    # Fetch emails from the database related to the account
    test_email = Email(sender="Root", recipient=acc.email, subject="Hello!", body="Hello World! How are you doing? I'm doing great!", sent_at=datetime.now(timezone.utc))
    
    # Simulate another account to test
    test_student2 = User(username="Dylan", email="dylan@example.com", password_hash="hashedpassword")

    # Commit the new account and email to the database
    db.session.add(test_student2)
    db.session.add(test_email)
    db.session.commit()

    # Simulate account list with one account fetched from the database
    test_account_list = [acc, test_student2]
    
    # Print a list of options for the user
    print(f"Hello {acc.username}.\n")
    while True:
        print("1. Check Inbox\n")
        print("2. Check For Unread Emails\n")
        print("3. Compose Email\n")
        print("4. Exit")
        user_input = input("Please give a numeric input from 1-4 to perform an action: ")
        if user_input == "1":
            check_email(acc)  # You can modify this to fetch emails from the database
        elif user_input == "2":
            check_for_unread_emails(acc)  # Modify this to check unread emails in the database
        elif user_input == "3":
            send_email(test_email, test_student2)
            # This could trigger email creation and DB commit
        elif user_input == "4":
            print("Goodbye!\n")
            break
        else:
            print("Error! Invalid input detected. Please try again.\n")
    return

# Entry point for the messaging system
def main():
    # Fetch or create a user from the database
    user = User.query.filter_by(username="Hunter").first()
    if not user:
        # If the user doesn't exist, create it and commit to the database
        user = User(username="Hunter", email="hunter@example.com", password_hash="hashedpassword")
        db.session.add(user)
        db.session.commit()

    manage_account(user)  # Pass the user object to manage the account
    return

if __name__ == "__main__":
    from project import create_app
    app = create_app()
    
    with app.app_context():
        main()