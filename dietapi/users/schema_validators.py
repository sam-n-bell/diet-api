from marshmallow import Schema, fields
from marshmallow.validate import Length

class RegisterSchema(Schema):
    email = fields.Email(required=True)
    first_name = fields.String(required=True, validate=Length(min=1))
    last_name = fields.String(required=True, validate=Length(min=1))
    password = fields.Str(required=True, validate=Length(min=8))

class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)


def validate_registration_post(registration_body):
    schema = RegisterSchema()
    return schema.validate(registration_body)

def validate_login_post(login_body):
    schema = LoginSchema()
    return schema.validate(login_body)
