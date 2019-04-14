# app/entity/__init__.py


# db variable initialization
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from app import app

db = SQLAlchemy(app)
ma = Marshmallow(app)