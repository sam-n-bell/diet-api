from recipeapi import db
from citext import CIText
from sqlalchemy.dialects.postgresql import UUID, NUMERIC
import uuid
from datetime import datetime

class RecipeReview(db.Model):
    __tablename__ = 'recipe_reviews'
    recipe_review_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    recipe_id = db.Column(UUID(as_uuid=True), db.ForeignKey('recipes.recipe_id'), nullable=False)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.user_id'), nullable=False)
    rating = db.Column(NUMERIC, nullable=False)
    review = db.Column(CIText(), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, recipe_id, user_id, rating, review):
        self.recipe_id = recipe_id
        self.user_id = user_id
        self.rating = rating
        self.review = review

    def __repr__(self):
        return f'RecipeReview(recipe_review_id: {self.recipe_review_id}, recipe_id: {self.recipe_id}, rating: {self.rating}, review: {self.review}, user_id: {self.user_id}, date_created: {self.date_created})'
