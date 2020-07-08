from flask import Blueprint
from recipeapi.recipereviews.models import RecipeReview

recipe_reviews = Blueprint('recipe-reviews', __name__)