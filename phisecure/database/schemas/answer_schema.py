from marshmallow import Schema, fields, validate


class AnswerSchema(Schema):
    """ Schema to validate the answer data

    Args:
        Schema (_type_): _description_
    """
    question_id = fields.Integer(required=True)
    answer_text = fields.String(required=True)