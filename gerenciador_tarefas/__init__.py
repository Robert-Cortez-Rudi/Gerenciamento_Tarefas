from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config, DevelopmentConfig, ProductionConfig
from routes import usuario


db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig) # Pode ser alterado para modo de desenvolvimento ou de produção

    db.init_app(app)

    with app.app_context(): # Insere contexto ao app para a criação das tabelas do banco de dados
        db.create_all() # Criação das tabelas no banco de dados

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    app.register_blueprint(usuario)

    return app