from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from gerenciador_tarefas.models.tasks import Task
from gerenciador_tarefas import db
from datetime import datetime
from gerenciador_tarefas.forms import CreateTaskForm, EditTaskForm

tasks = Blueprint("tasks", __name__)


@tasks.route("/dashboard")
@login_required
def dashboard():
    user_tasks = Task.query.filter_by(id=current_user.id).all()
    return render_template("dashboard.html", tasks=user_tasks, title="Suas Tarefas")


@tasks.route("/dashboard/new_task", methods=["GET", "POST"])
@login_required
def create_task():
    if request.method == "POST":

        form = CreateTaskForm()
        if form.validate_on_submit():
            try:
                form.due_date.data = datetime.strptime("%d-%m-%Y")
            except ValueError:
                flash("Data invalida! Use o formato DD-MM-YYYY.", "danger")
                return redirect(url_for("tasks.create_task"))

            new_task = Task(
                title=form.title.data,
                description=form.description.data,
                due_date=form.due_date.data,
                user_id = current_user.id
            ) 

            db.session.add(new_task)
            db.commit()
            flash("Tarefa criada com sucesso!", "success")
            return redirect(url_for("tasks.dashboard"))
    return render_template("task_form.html")


@tasks.route("/dashboard/<int:id>/delete/")
@login_required
def delete_task(id):
    task = Task.query.get_or_404(id)
    if task != current_user.id:
        flash("Você não tem permissão para deletar essa tarefa!", "danger")
        return redirect(url_for("tasks.dashboard"))
    
    db.session.delete(task)
    db.session.commit()
    flash("Tarefa deletada com sucesso!", "success")
    return redirect(url_for("tasks.dashboard"))


@tasks.route("/dashboard/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit_task(id):
    if request.method == "POST":
        task = Task.query.get_or_404(id)
        if task != current_user.id:
            flash("Você não tem permissão para editar essa tarefa!", "danger")
            return redirect(url_for("tasks.dashboard"))
        
        form = EditTaskForm()
        if form.validate_on_submit():
            task.title = form.title.data
            task.description = form.description.data
            task.due_date = form.due_date.data

        Task.query.filter_by(id=id).update({
            "title": task.title,
            "description": task.description,
            "due_date": task.due_date
        })
        db.session.commit()
        flash("A sua tarefa foi atualizada com sucesso!", "success")
        return redirect(url_for("tasks.dashboard"))
    return render_template("edit_task.html", """form=form - ARRUMAR""", task=task)
    

@tasks.route("/dashboard/completed/<int:id>", methods=["GET", "POST"])
def task_completed(id):
    task = Task.query.get_or_404(id)
    if task != current_user.id:
        flash("Você não tem permissão para finalizar essa tarefa!", "danger")
    
    task.completed = True

    db.session.commit()
    flash("Tarefa finalizada com sucesso!", "success")
    return redirect(url_for("tasks.dashboard"))

