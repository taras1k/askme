import os
from os import environ
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = environ.get('SECRET_KEY')

SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_MIGRATE_REPO = environ.get('SQLALCHEMY_MIGRATE_REPO')
DEBUG = environ.get('DEBUG', True)

