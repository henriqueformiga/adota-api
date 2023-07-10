from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from app.database import setup_database
from app.routes import register_auth_routes
from app.security import setup_security
load_dotenv()


app = Flask(__name__)
setup_security(app)
setup_database(app)


register_auth_routes(app)
if __name__ == '__main__':
    app.run()
