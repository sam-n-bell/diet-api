from recipeapi.recipes.models import Recipe
from recipeapi import db

def save_new_recipe(body, uploaded_by):
    recipe = Recipe(name=body.get('name'),
                    instructions=body.get('instructions'),
                    ingredients=body.get('ingredients'),
                    utilities=body.get('utilities'),
                    est_completion_time_hrs=body.get('est_completion_time_hrs'),
                    min_serving_size=body.get('min_serving_size'),
                    max_serving_size=body.get('max_serving_size'),
                    user_id=uploaded_by)
    db.session.add(recipe)
    db.session.commit()

def get_recipe(recipe_id):
    return Recipe.query.filter_by(recipe_id=recipe_id).first()


def update_recipe(existing_recipe, body):
    existing_recipe.name = body.get('name')
    existing_recipe.instructions = body.get('instructions')
    existing_recipe.ingredients = body.get('ingredients')
    existing_recipe.utilities = body.get('utilities')
    existing_recipe.est_completion_time_hrs = body.get('est_completion_time_hrs')
    existing_recipe.min_serving_size = body.get('min_serving_size')
    existing_recipe.max_serving_size = body.get('max_serving_size')
    db.session.commit()

# https://stackoverflow.com/a/27159298/7858114
def delete_recipe(recipe_id):
    Recipe.query.filter_by(recipe_id=recipe_id).delete()
    db.session.commit()