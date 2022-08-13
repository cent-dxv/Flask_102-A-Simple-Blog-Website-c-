from .view import post
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model , UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    username = db.Column(db.String(120),)
    password = db.Column(db.String(120), unique=True)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    post_text =db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now()) 