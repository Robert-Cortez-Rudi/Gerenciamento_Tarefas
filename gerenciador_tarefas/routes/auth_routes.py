from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_required, logout_user, login_user
from gerenciador_tarefas.models.user import User
from gerenciador_tarefas import login_manager, db
from gerenciador_tarefas.forms import LoginForm, RegisterForm


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
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and user.check_password(user.password, form.password.data):
                login_user(user)
                return redirect(url_for("usuario.principal"))
            else:
                return render_template("login.html", error="E-mail ou senha incorretos")
    return render_template("login.html")


@usuario.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        form = RegisterForm()
        if form.validate_on_submit():
            if form.password.data == form.confirm_password.data:
                user_exists = User.query.filter_by(email=form.email.data).first()
                if user_exists is None:
                    new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)

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
