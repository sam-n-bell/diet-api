from marshmallow import Schema, fields
from marshmallow.validate import Length, Range

class RecipeReviewSchema(Schema):
    review = fields.String(validate=Length(min=3, max=300), required=True)
    rating = fields.Float(validate=Range(min=0.0, max=5.0), required=True)
    recipe_id = fields.String(required=True)

def validate_recipe_review(review_body):
    schema = RecipeReviewSchema()
    return schema.validate(review_body)