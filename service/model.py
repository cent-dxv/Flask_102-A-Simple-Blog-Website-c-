from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model , UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    username = db.Column(db.String(120),)
    password = db.Column(db.String(120), unique=True)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    post =db.relationship('Post' , backref='user' , passive_deletes =True)
    Comments =db.relationship('Comment' , backref='user' , passive_deletes =True)



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_text =db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    author = db.Column(db.Integer , db.ForeignKey('user.id' ,ondelete="CASCADE") ,nullable=False)
    Comments =db.relationship('Comment' , backref='post' , passive_deletes =True)



class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    author = db.Column(db.Integer, db.ForeignKey('user.id',ondelete="CASCADE"), nullable=False)
    post_id =db.Column(db.Integer, db.ForeignKey('post.id',ondelete="CASCADE"), nullable=False)
    text = db.Column(db.String(255), nullable=False)