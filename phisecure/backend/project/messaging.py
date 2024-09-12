"""
messaging.py
Team Orange
Last Modified: 9/12/24
Purpose: Contains logic for messaging between accounts and their email environments
"""

# from flask import Flask
from account import Account
from email import Email

# app = Flask(__name__)

def manage_account(acc):
    """
    Function that manages the given account
    :param acc: The current user's account
    :returns: N/A
    """
    user_input = ""
    test_email = Email("Hello!", "Root", "Dylan", "Hello World! How are you doing? I'm doing great!")
    test_student2 = Account("Dylan", [test_email]) 
    test_account_list = [acc, test_student2, Account("Ethan"), Account("Ralph"), Account("Joshua")]

    # Print a list of options for the user
    print("Hello " + acc.name + ".\n")
    while(True):
        print("1. Check Inbox\n")
        print("2. Check For Unread Emails\n")
        print("3. Compose Email\n")
        print("4. Exit")
        user_input = input("Please give a numeric input from 1-4 to perform an action: ")
        if(user_input == "1"):
            acc.check_email()
        elif(user_input == "2"):
            acc.check_for_unread_emails()
        elif(user_input == "3"):
            acc.make_email(test_account_list)
        elif(user_input == "4"):
            print("Goodbye!\n")
            break
        else:
            print("Error! Invalid input detected. Please try again.\n")
    return

def main():
    test_student1 = Account("Hunter")
    manage_account(test_student1) 
    return

if __name__ == "__main__":
    main()