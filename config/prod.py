import os

DEBUG = False
SECRET_KEY = os.urandom(24).hex()
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:2012@localhost/catalog_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
