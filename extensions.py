from flask.ext.babel import Babel
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin import Admin

db = SQLAlchemy()
babel = Babel()
admin = Admin()
