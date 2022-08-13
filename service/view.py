from flask import Blueprint, render_template, redirect, url_for,request,flash
from flask_login import login_required ,current_user


view = Blueprint("view", __name__)
@view.route("/")
@view.route("/home")
@login_required
def home():
    print(current_user.username)
    return render_template('home.html', user = current_user)

@view.route("/post" , methods =[ 'POST' , 'GET' ])
@login_required
def post():
    if request.method == 'POST':
        text = request.form.get('text')
        if not text:
            flash('Post can not be empty', catagory = 'error')
        else:
            flash('Post successfully created ' , catagory = 'success')

    
    return render_template('create_post.html', user = current_user)