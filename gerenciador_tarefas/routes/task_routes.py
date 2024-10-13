from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from gerenciador_tarefas.models.tasks import Task
from gerenciador_tarefas import db
from datetime import datetime

tasks = Blueprint("tasks", __name__)

@tasks.route("/dashboard")
@login_required
def dashboard():
    user_tasks = Task.query.filter_by(id=current_user.id).all()
    return render_template("dashboard.html", tasks=user_tasks)

@tasks.route("dashboard/new_task", methods=["GET", "POST"])
@login_required
def create_task():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        due_date = request.form["due_date"]

        try:
            due_date = datetime.strptime("%Y-%m-%d")
        except ValueError:
            flash("Data invalida! Use o formato YYYY-MM-DD.", "danger")
            return redirect(url_for("tasks.create_task"))

        new_task = Task(
            title=title,
            description=description,
            due_date=due_date,
            user_id = current_user.id
        ) 

        db.session.add(new_task)
        db.commit()
        flash("Tarefa criada com sucesso!", "success")
        return redirect(url_for("tasks.dashboard"))
    return render_template("task_form.html")


@tasks.route("dashboard/delete")
@login_required
def delete_task():
    task = Task.query.get_or_404(id)
    if task != current_user.id:
        flash("Você não tem permissão para deletar essa tarefa!", "danger")
        return redirect(url_for("tasks.dashboard"))
    
    db.session.delete(task)
    db.session.commit()
    flash("Tarefa deletada com sucesso!", "success")
    return redirect(url_for("tasks.dashboard"))

