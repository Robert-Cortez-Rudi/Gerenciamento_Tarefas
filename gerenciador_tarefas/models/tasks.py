from gerenciador_tarefas import db
from datetime import datetime, timezone
from flask_login import UserMixin

class Task(UserMixin, db.Model):
    __tablename__ = "Tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False) # Data de vencimento da tarefa
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey("Users.id"), nullable=False)
    created_at  = db.Column(db.DateTime, default=datetime.now(timezone.utc)) # Data de criação


    def task_completed(self): # Tarefa finalizada
        self.completed = True

    def is_overdue(self): # Verifica se a tarefa está atrasada
        return datetime.now(timezone.utc) > self.due_date and not self.completed
    
    def delete_task(self):
        db.session.delete(self)
        db.commit()

    def set_due_date(self, new_date): # Muda a data do prazo 
        self.due_date = new_date
        db.session.commit()

    def __repr__(self):
        return f"Task {self.title}"
