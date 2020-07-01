from flask import Flask, blueprints, Response, jsonify
from dietapi.configs.production_configuration import ProductionConfig
from dotenv import load_dotenv
import os
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
load_dotenv()

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
migrate = Migrate()
jwt = JWTManager()

def create_app(config=ProductionConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    prefix = os.getenv("URL_PREFIX")

    db.__init__(app)
    ma.__init__(app)
    bcrypt.__init__(app)
    migrate.__init__(app, db)
    jwt.__init__(app)

    from dietapi.users.routes import users
    app.register_blueprint(users, url_prefix=prefix)

    @app.route('/', methods=['GET'])
    def return_index():
        return Response("Index")

    @app.errorhandler(400)
    def bad_request(e):
        return jsonify(message=e.description), 400

    @app.errorhandler(401)
    def unauthorized(e):
        return jsonify(message=e.description), 401

    @app.errorhandler(404)
    def resource_not_found(e):
        return jsonify(message=e.description), 404

    @app.errorhandler(500)
    def internal_system_error(e):
        return jsonify(message=e.description), 500

    return app
