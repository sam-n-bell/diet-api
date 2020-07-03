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