from flask import Blueprint, render_template, redirect, url_for


view = Blueprint("view", __name__)

@view.route("/")
@view.route("/home")
def home():
    return f"you are at {__name__}"