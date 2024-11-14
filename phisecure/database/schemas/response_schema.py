from marshmallow import Schema, fields, validate
from database.schemas.answer_schema import AnswerSchema

class ResponseSchema(Schema):
    """ Schema to validate the response data

    Args:
        Schema (_type_): _description_
    """
    questionnaire_id = fields.Integer(required=True)
    student_id = fields.Integer(required=True)
    answers = fields.List(fields.Nested(AnswerSchema), required=True)
    