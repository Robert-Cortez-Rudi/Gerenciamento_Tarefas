from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_required, logout_user, login_user
from gerenciador_tarefas.models.user import User
from gerenciador_tarefas import login_manager, db


usuario = Blueprint("usuario", __name__)

@usuario.route("/")
def principal():
    return render_template("index.html")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@usuario.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for("usuario.principal"))
        else:
            return render_template("login.html", error="E-mail ou senha incorretos")
    return render_template("login.html")


@usuario.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        name = request.form["nome"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password == confirm_password:
            user_exists = User.query.filter_by(email=email).first()
            if user_exists is None:
                new_user = User(username=name, email=email, password=password)

                db.session.add(new_user)
                db.session.commit()
                flash("Cadastro realizado com sucesso!", "success")
                login_user(new_user)
                return redirect(url_for("usuario.principal"))
    return render_template("cadastro.html")


@usuario.route("/logout")
@login_required
def logout():
    logout_user()
    session.pop("user", None)
    flash("Você saiu da sua conta!", "success")
    return redirect(url_for("usuario.principal"))
