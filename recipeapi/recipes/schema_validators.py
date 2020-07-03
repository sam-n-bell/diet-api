from marshmallow import Schema, fields
from marshmallow.validate import Length

class IngredientsSchema(Schema):
    quantity: fields.Int()
    description: fields.String()

class UtilitySchema(Schema):
    description: fields.String()

class RecipeSchema(Schema):
    name = fields.String(required=True, validate=Length(min=1))
    instructions = fields.String(required=True, validate=Length(min=1))
    # https://stackoverflow.com/questions/59198428/validate-list-of-schemas-with-constraints-for-list-length-using-marshmallow
    ingredients = fields.List(fields.Nested(IngredientsSchema, required=True, validate=Length(min=1)))
    utilities = fields.List(fields.Nested(UtilitySchema, required=True, validate=Length(min=1)))


def validate_recipe_post(recipe_body):
    schema = RecipeSchema()
    return schema.validate(recipe_body)