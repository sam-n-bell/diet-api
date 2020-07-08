from recipeapi.recipereviews.models import RecipeReview
from recipeapi import db

def save_new_review(body, uploaded_by):
    review = RecipeReview(review=body.get('review'),
                          rating=body.get('rating'),
                          recipe_id=body.get('recipe_id'),
                          user_id=uploaded_by)
    db.session.add(review)
    db.session.commit()