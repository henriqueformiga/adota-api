import os
from pymongo import MongoClient


def setup_database(app):
    client = MongoClient(os.getenv('MONGODB_URL'))
    app.db = client['adota']