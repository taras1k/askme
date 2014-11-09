import os
from os import environ

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
BACKGROUND_IMAGES_DIRR = os.path.join(BASE_DIR, 'static/background_images')
SECRET_KEY = environ.get('SECRET_KEY')

SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_MIGRATE_REPO = environ.get('SQLALCHEMY_MIGRATE_REPO')
DEBUG = environ.get('DEBUG', True)

BABEL_DEFAULT_LOCALE = 'uk'
