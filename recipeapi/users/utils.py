from recipeapi import ma

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose https://flask-marshmallow.readthedocs.io/en/latest/
        fields = ("email", "first_name", "last_name", "user_id")

def serialize_many(users):
    user_schema = UserSchema()
    return user_schema.dump(users, many=True)

def serialize_one(user):
    user_schema = UserSchema()
    return user_schema.dump(user, many=False)
