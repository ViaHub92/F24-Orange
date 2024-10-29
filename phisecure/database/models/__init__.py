"""
imports all the models from the database in models folder
"""

from database.models.role import Role
from database.models.user_interaction import UserInteraction
from database.models.email import Email
from database.models.inbox import Inbox
from database.models.course import Course
from database.models.admin import Admin
from database.models.instructor import Instructor
from database.models.student import Student
from database.models.template import Template
from database.models.user_responses import UserResponses
from database.models.phishing_email import PhishingEmail
from database.models.questionnaire import Questionnaire, Question, Response

