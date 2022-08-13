from flask import Blueprint, render_template, redirect, url_for,request,flash
from flask_login import login_required ,current_user

from service import auth
from .model import Post
from . import db

view = Blueprint("view", __name__)
@view.route("/")
@view.route("/home")
@login_required
def home():
    post = Post.query.all()
    print(post)
    return render_template('home.html', user = current_user)

@view.route("/post" , methods =[ 'POST' , 'GET' ])
@login_required
def post():
    if request.method == 'POST':
        text = request.form.get('text')
        if not text:
            flash('Post can not be empty', category = 'erorr')
        else:
            new_post = Post(post_text=text , author =current_user.id)
            db.session.add(new_post)
            db.session.commit()
            flash('Post successfully created ' , category = 'success')
            redirect('/')

    
    return render_template('create_post.html', user = current_user)