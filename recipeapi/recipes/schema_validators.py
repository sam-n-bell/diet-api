from marshmallow import Schema, fields
from marshmallow.validate import Length, Range

class IngredientsSchema(Schema):
    quantity = fields.Float(required=True, validate=Range(min=0.1))
    description = fields.String(required=True, validate=Length(min=2))

class RecipeSchema(Schema):
    name = fields.String(required=True, validate=Length(min=1))
    instructions = fields.String(required=True, validate=Length(min=1))
    # https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html?highlight=nested#marshmallow.fields.Nested.schema
    ingredients = fields.List(fields.Nested(IngredientsSchema), required=True, validate=Length(min=1))
    utilities = fields.List(fields.String(), required=True, validate=Length(min=1))
    est_completion_time_hrs = fields.Float(required=True, validate=Range(min=0.0))
    min_serving_size = fields.Integer(required=True, validate=Range(min=1))
    max_serving_size = fields.Integer(required=False, validate=Range(min=1))


def validate_recipe_post(recipe_body):
    schema = RecipeSchema()
    return schema.validate(recipe_body)