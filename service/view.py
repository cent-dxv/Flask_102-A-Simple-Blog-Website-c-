from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required ,current_user


view = Blueprint("view", __name__)
@view.route("/")
@view.route("/home")
@login_required
def home():
    print(current_user.username)
    return render_template('home.html', user = current_user)

@view.route("/post")
@login_required
def post():
    print(current_user.username)
    return render_template('post.html', user = current_user)