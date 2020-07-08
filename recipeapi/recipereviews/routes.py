from flask import Blueprint, Response, request, abort
from recipeapi.marshmallow_utils import convert_errors_to_sentence
from recipeapi.recipereviews.models import RecipeReview
from recipeapi.recipereviews.schema_validators import validate_recipe_review
from flask_jwt_extended import jwt_required, get_jwt_identity
from recipeapi.recipes.services import get_recipe
from recipeapi.recipes.schema_validators import RecipeSchema
from recipeapi.recipereviews.services import save_new_review
recipe_reviews = Blueprint('recipe-reviews', __name__)


@recipe_reviews.route('/recipe-reviews', methods=['POST'])
@jwt_required
def create():
    current_user = get_jwt_identity()
    body = request.json
    errors = validate_recipe_review(body)
    if errors:
        abort(400, description=convert_errors_to_sentence(errors))

    recipe = get_recipe(body.get('recipe_id'))
    recipe_schema = RecipeSchema()
    recipe = recipe_schema.dump(recipe)
    if current_user.get('user_id') == recipe.get('user_id'):
        abort(400, description="You cannot review your own recipe")
    save_new_review(body, current_user.get('user_id'))

    return Response(None, 200)