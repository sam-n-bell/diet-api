from flask import Blueprint, request, Response, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from recipeapi.recipes.models import Recipe
from recipeapi.recipes.schema_validators import validate_recipe_post
from recipeapi.marshmallow_utils import convert_errors_to_sentence

recipes = Blueprint('recipes', __name__)

@recipes.route('/recipes', methods=['POST'])
@jwt_required
def create_recipe():
    body = request.json
    errors = validate_recipe_post(body)
    if errors:
        abort(400, description=convert_errors_to_sentence(errors))
    user = get_jwt_identity()
    return Response(None, 200)