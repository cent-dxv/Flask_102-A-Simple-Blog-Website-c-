from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required


view = Blueprint("view", __name__)
@view.route("/")
@view.route("/home")
@login_required
def home():
    return render_template('home.html')