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
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                session["user"] = user.username
                return redirect(url_for("tasks.dashboard"))
            else:
                flash("Email ou senha inválidos", "danger")
        else:
            flash("Email ou senha inválidos", "danger")
    return render_template("login.html", form=form)


@usuario.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    form = RegisterForm()
    if request.method == "POST":
        if form.validate_on_submit():
            if form.password.data == form.confirm_password.data:
                user_exists = User.query.filter_by(email=form.email.data).first()
                if user_exists is None:
                    user = User(username=form.username.data, email=form.email.data, password=form.password.data)

                    db.session.add(user)
                    db.session.commit()
                    login_user(user)
                    session["user"] = user.username
                    return redirect(url_for("tasks.dashboard"))
                else:
                    flash("⚠️ Este email já está em uso. Tente outro!", "danger")
            else:
                flash("❌ As senhas não conferem! Verifique e tente novamente.", "danger")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f"Erro no campo {field}: {error}", "danger")
    return render_template("cadastro.html", form=form)


@usuario.route("/logout")
@login_required
def logout():
    logout_user()
    session.pop("user", None)
    return redirect(url_for("usuario.principal"))


@usuario.route("/<int:id>/delete")
@login_required
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    session.clear()
    flash("Conta excluida com sucesso!", "success")
    return redirect(url_for("usuario.principal"))