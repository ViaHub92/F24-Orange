"""
email.py
Team Orange
Last Modified: 9/12/24
Purpose: Contains data for Email object
"""

class Email:
    """
    An account with a name and inbox of emails
    """
    def __init__(self, subject="Test", sender="John Doe", recipient="Jane Doe", body="Testing!", read = False):
        self._subject = subject
        self._sender = sender
        self._recipient = recipient
        self._body = body
        self._read = read
    
    @property
    def subject(self):
        return self._subject
    
    @subject.setter
    def subject(self, subject):
        self._subject = subject
    
    @property
    def sender(self):
        return self._sender
    
    @sender.setter
    def sender(self, sender):
        self._sender = sender
    
    @property
    def recipient(self):
        return self._recipient
    
    @recipient.setter
    def recipient(self, recipient):
        self._recipient = recipient
    
    @property
    def body(self):
        return self._body
    
    @body.setter
    def body(self, body):
        self._body = body
    
    @property
    def read(self):
        return self._read
    
    @read.setter
    def read(self, read):
        self._read = read
    
    def __str__(self):
        temp = "Subject of Email: " + self._subject + "\n"
        temp += "Email Sender: " + self._sender + "\n"
        temp += "Email Recipient: " + self._recipient + "\n"
        temp += "Email Body: " + self._body + "\n"
        temp += "Email is Read: " + str(self._read) + "\n"
        return temp
