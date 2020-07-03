from recipeapi import db, ma
from datetime import datetime
from citext import CIText
from sqlalchemy.dialects.postgresql import UUID, JSONB, NUMERIC, ARRAY, TEXT

import uuid

# https://stackoverflow.com/a/49398042/7858114 UUID
class Recipe(db.Model):
    __tablename__ = 'recipes'
    recipe_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = db.Column(CIText(), nullable=False)
    ingredients = db.Column(JSONB, nullable=False)
    instructions = db.Column(CIText(), nullable=False)
    utilities = db.Column(ARRAY(TEXT))
    est_completion_time_hrs = db.Column(NUMERIC, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    last_updated = db.Column(db.DateTime)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.user_id'), nullable=False)

    def __repr__(self):
        return f'Recipe(recipe_id: {self.recipe_id}, name: {self.name}, ingredients: {self.ingredients}, instructions: {self.instructions}, utilities: {self.utilities}, date_created: {self.date_created}, last_updated: {self.last_updated},  est_completion_time_hrs: {self.est_completion_time_hrs}, user_id: {self.user_id})'
