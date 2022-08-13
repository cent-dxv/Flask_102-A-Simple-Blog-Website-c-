from gettext import find
from flask import Blueprint, render_template, redirect, url_for,request,flash
from flask_login import login_required ,current_user

from service import auth
from .model import Post, User
from . import db

view = Blueprint("view", __name__)
@view.route("/")
@view.route("/home")
@login_required
def home():
    post = Post.query.all()
    print(post)
    return render_template('home.html', user = current_user , posts =post)

@view.route("/post/" , methods =[ 'POST' , 'GET'])
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

@view.route("/remove-post/<id>" , methods =[ 'GET' ])
def delete_post(id):
    deleted_post = Post.query.filter_by(id=id).first()

    if not deleted_post:
        flash("Post dosen't  exist" , category='erorr')
    elif current_user.id != deleted_post.user.id:
        flash("an Authorized access denied", category='erorr')
    else:
        db.session.delete(deleted_post)
        db.session.commit()
        flash("Post removed", category='success')
    return redirect('/')

@view.route("/<name>")
@login_required
def post_by_user(name):
    user = User.query.filter_by(username=name).first()

    if not user:
        flash("User does not exist", category='error')
        return redirect('/')
    
    post = Post.query.filter_by(author=user.id).all()
    return render_template('home.html', user = current_user , posts =post)
