from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import LoginManager, login_required, logout_user, current_user
from models.user import User

usuario = Blueprint("usuario", __name__)

@usuario.route("/")
def principal():
    return render_template("index.html")

