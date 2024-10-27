from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class CreateTaskForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=1, max=255)])
    description = TextAreaField("Description", validators=[DataRequired()])
    due_date = DateField("Due date", format="%Y-%m-%d" , validators=[DataRequired()])
    submit = SubmitField("Criar Tarefa")


class EditTaskForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=1, max=255)])
    description = TextAreaField("Description", validators=[DataRequired()])
    due_date = DateField("Due date", format="%Y-%m-%d" , validators=[DataRequired()])
    submit = SubmitField("Salvar Alterações")
