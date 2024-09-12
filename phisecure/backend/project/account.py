"""
account.py
Team Orange
Last Modified: 9/12/24
Purpose: Contains data for Account object
Most of the data currently is temporary data to work out the logic. The specifics will come later.
"""

from email import Email

class Account:
    """
    An account with a name and inbox of emails
    """
    def __init__(self, name="John Doe", inbox = None):
        self._name = name
        if inbox is None:
            self._inbox = []
        else:
            self._inbox = inbox
    
    @property
    def name(self):
        return self._name
    
    @property
    def inbox(self):
        return self._inbox
    
    def __str__(self):
        temp = "Name of Account: " + self._name + "\n"
        temp += "Amount of Emails: " + str(len(self._inbox))
        return temp
    
    def check_email(self):
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
    
    def check_for_unread_emails(self):
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
    
    def add_to_inbox(self, email):
        """
        Adds a new email to the inbox of a given Account
        :param self: The account object to add an email to
        :param email: The email to be sent
        :yields: This object with a new email appended to the end of the inbox
        """
        self._inbox.append(email)
        return
    
    def send_email(self, email, account_list):
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
    
    def make_email(self, account_list):
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
    
