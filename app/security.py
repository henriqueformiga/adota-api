import os
from flask_cors import CORS
from flask_jwt_extended import JWTManager


def setup_security(app):
    app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')
    CORS(app)
    jwt = JWTManager(app)