from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    paswword = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=6),
            EqualTo("paswword_confirm", message="As senhas não coincidem")
        ]
    )
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Cadastrar")
