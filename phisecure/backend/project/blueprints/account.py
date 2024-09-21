from flask import Blueprint, request, jsonify
from project import db
from project.models import User, Role, Inbox
"""
account.py
Team Orange
Last Modified: 9/21/24
Purpose: Creation and management of user accounts.
"""
account = Blueprint('account', __name__)

@account.route('/create_user', methods=['POST'])
def create_user():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password_hash = data.get('password_hash')
    first_name = data.get('first_name', '')
    last_name = data.get('last_name', '')

    # Check if user already exists
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({"message": "User already exists"}), 400

    # Create a default role if it doesn't exist (You might want to adjust this based on your actual role handling)
    default_role = Role.query.first()  # Assumes there is at least one role in the database
    if not default_role:
        default_role = Role(name='User')
        db.session.add(default_role)
        db.session.commit()

    # Create inbox for the user
    inbox = Inbox()
    db.session.add(inbox)
    db.session.commit()

    # Create new user
    new_user = User(
        username=username,
        email=email,
        password_hash=password_hash,
        first_name=first_name,
        last_name=last_name,
        role_id=default_role.id,  # Set default role id
        inbox_id=inbox.id  # Set the created inbox id
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully!"}), 201

@account.route('/get_user/<username>', methods=['GET'])
def get_user(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name
        }), 200
    else:
        return jsonify({"message": "User not found"}), 404

@account.route('/list_users', methods=['GET'])
def list_users():
    users = User.query.all()
    if users:
        user_list = [{
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name
        } for user in users]
        return jsonify(user_list), 200
    else:
        return jsonify({"message": "No users found"}), 404

    #def check_email(self):
        """
        Checks the inbox of the account for any emails.
        :param self: The account object
        :return: N/A
        """
        if len(self._inbox) == 0:
            print("No emails to speak of!")
        else:
            for i in range(len(self._inbox)):
                print(self._inbox[i])
        return
    
    #def check_for_unread_emails(self):
        """
        Checks the inbox of the account for any unread emails
        :param self: the account object
        :return: N/A
        """

        # First, check the inbox to see if it has any emails. If not, simply print a message
        # If not, then check all the emails to see if they are unread or not.
        if len(self._inbox) == 0:
            print("No emails to speak of!")
        else:
            temp_count = 0
            for i in range(len(self._inbox)):
                if(self._inbox[i].read is False):
                    temp_count += 1
            if(temp_count == 0):
                print("You have no unread messages.")
            else:
                user_input = ""
                print("You have " + str(temp_count) + " unread messages.\n")   
                print()
                # Ask the user if they want to see the unread messages or not
                while(True):
                    user_input = input("Would you like to read the unread emails? Y or N: ")
                    if user_input == "Y" or user_input == "y":
                        for i in range(len(self._inbox)):
                            if(self._inbox[i].read is False):
                                print(self._inbox[i])
                                self._inbox[i].read = True
                        break
                    elif user_input == "N" or user_input == "n":
                        break
                    else:
                        print("Error! Invalid input detected! Please try again.\n")
        return
    
    #def add_to_inbox(self, email):
        """
        Adds a new email to the inbox of a given Account
        :param self: The account object to add an email to
        :param email: The email to be sent
        :yields: This object with a new email appended to the end of the inbox
        """
        self._inbox.append(email)
        return
    
    #def send_email(self, email, account_list):
        """
        Sends the email to the recipient of the email
        :param self: The account object sending the email
        :param email: The email to be sent
        :param account_list: List of valid accounts that emails can be sent to
        :return: N/A
        """
        if len(account_list) == 0:
            print("Error! No valid accounts could be found. Check server status. Email could not be sent.")
        else:
            for i in range(len(account_list)):
                if(email.recipient == account_list[i].name):
                    account_list[i].add_to_inbox(email)
                    print("Email successfully sent.")
                    return
            print("Error! Invalid recipient. Please check the recipient of the email and try again.")
        return
    
    #def make_email(self, account_list):
        """
        Forms an Email to be sent to the recipient
        :param self: The account object
        :param self: The list of valid accounts. Will be passed to send_email.
        :yields: An email to be sent to the recipient through the send_email function
        """
        subject = ""
        sender = self.name
        recipient = ""
        body = ""

        subject = input("Please give the subject of the email: ")
        recipient = input("Please give the recipient of the email: ")
        body = input("Please give the body of the email: ")

        temp_email = Email(subject, sender, recipient, body)
        self.send_email(temp_email, account_list)
    
