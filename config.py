import os
from os import environ

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
BACKGROUND_IMAGES_DIRR = os.path.join(BASE_DIR, 'static/background_images')
SECRET_KEY = environ.get('SECRET_KEY')

SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')
DEBUG = False
if DEBUG:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')

BABEL_DEFAULT_LOCALE = 'uk'
JQUERY_CDN_URL = '//ajax.googleapis.com/ajax/libs/jquery/'
ANSWERS_DIR = os.path.join(BASE_DIR, 'answers')
