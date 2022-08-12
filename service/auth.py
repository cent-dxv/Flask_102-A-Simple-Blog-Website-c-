from flask import Blueprint, render_template, redirect, url_for


auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return "login"


@auth.route("/logout")
def logout():
    return "logout"

@auth.route("/signup")
def signup():
    return "signup"