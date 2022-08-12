
from urllib import request
from flask import Blueprint, render_template, redirect, url_for ,request,flash
from .model import User
from . import db
from flask_login import login_user  , logout_user , login_required , current_user
from werkzeug.security import generate_password_hash  , check_password_hash

auth = Blueprint("auth", __name__)

@auth.route("/login" , methods = ['POST' ,'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user =  User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password , password):
                flash('loged in')
                login_user(user, remember=True)
                return redirect(url_for('view.home'))
            else:
                flash("Icorrect user name or password !" ,category='erorr')
        else:
            flash("user dose not  exist" , category='erorr')
        

    return render_template('login.html')


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("view.home"))


@auth.route("/sign-up" , methods = ['GET' ,'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        print(f"name{username} , {email} , {password1} , {password2}")

        #check if user alrady exist
        email_exist = User.query.filter_by(email =email).first()
        user_name_exist = User.query.filter_by(username =username).first()

        if email_exist:
            flash('Email already exists ' , category='erorr')
        elif user_name_exist:
            flash('username already in use try other username ' , category = 'erorr') 
        elif password1  != password2 :
            flash('password don\'t match! '  ,category = 'erorr')
        elif len(password1) < 6:
            flash('Password length too short! at least use 6 or above',category = 'erorr')
        elif len(username) < 2:
            print(f" user name is {username} and length {len(username)}")
            flash('Username too short !  user name must be 3 or above',category = 'erorr')
        elif len(email) < 4:
            flash('Invalid email address ! ',category='erorr')
        else:
            new_user = User(email= email , username= username , password= generate_password_hash(password1 , method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash(f" we'r gald to see you {username} ")
            redirect('/')
    
    return render_template('sign-up.html')