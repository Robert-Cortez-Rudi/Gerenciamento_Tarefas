from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(message="O nome de usuário é obrigatório")])
    email = StringField(
        "Email", 
        validators=[
            DataRequired(message="O email é obrigatório!"), 
            Email(message="Forneça um email válido!")
        ]
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(message="Insira a senha"),
            Length(min=6, message="A senha deve ter no mínimo 6 digitos"),
        ]
    )
    confirm_password = PasswordField(
        "Confirm Password", 
        validators=[DataRequired(message="A confirmação da senha é obrigatória"), 
                    EqualTo("confirm_password", message="As senhas não coincidem")
                    ]
        )
    submit = SubmitField("Cadastrar")
