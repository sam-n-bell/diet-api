from flask import Flask, blueprints, Response
from dietapi.configs.production_configuration import ProductionConfig
from dotenv import load_dotenv
import os
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
load_dotenv()

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
migrate = Migrate()

def create_app(config=ProductionConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    prefix = os.getenv("URL_PREFIX")

    db.__init__(app)
    ma.__init__(app)
    bcrypt.__init__(app)
    migrate.__init__(app, db)

    from dietapi.users.routes import users
    app.register_blueprint(users, url_prefix=prefix)

    @app.route('/', methods=['GET'])
    def return_index():
        return Response("Index")

    return app
