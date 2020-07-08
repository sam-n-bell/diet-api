from flask import Blueprint, request, Response, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from recipeapi.recipes.models import Recipe
from recipeapi.recipes.schema_validators import validate_recipe_post
from recipeapi.marshmallow_utils import convert_errors_to_sentence
from recipeapi.recipes.services import save_new_recipe, get_recipe, update_recipe, delete_recipe

recipes = Blueprint('recipes', __name__)


@recipes.route('/recipes', methods=['POST'])
@jwt_required
def create():
    body = request.json
    errors = validate_recipe_post(body)
    if errors:
        abort(400, description=convert_errors_to_sentence(errors))
    user = get_jwt_identity()
    save_new_recipe(body, user.get('user_id'))
    return Response(None, 201)

@recipes.route('/recipes/<recipe_id>', methods=['PATCH'])
@jwt_required
def patch(recipe_id):
    body = request.json
    # make sure someone else isn't updating record
    logged_in_user = get_jwt_identity()
    existing_recipe = get_recipe(recipe_id)
    if logged_in_user.get('user_id') != str(existing_recipe.user_id):
        abort(401, description='You do not have permission to do that.')
    update_recipe(existing_recipe, body)
    return Response(None, 200)

@recipes.route('/recipes/<recipe_id>', methods=['DELETE'])
@jwt_required
def delete(recipe_id):
    body = request.json
    # make sure someone else isn't updating record
    logged_in_user = get_jwt_identity()
    existing_recipe = get_recipe(recipe_id)
    if logged_in_user.get('user_id') != str(existing_recipe.user_id):
        abort(401, description='You do not have permission to do that.')
    delete_recipe(recipe_id)
    return Response(None, 200)