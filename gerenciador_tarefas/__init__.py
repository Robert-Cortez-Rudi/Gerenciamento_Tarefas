from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config, DevelopmentConfig, ProductionConfig


db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    print("App criado")
    app.config.from_object(ProductionConfig) # Pode ser alterado para modo de desenvolvimento ou de produção

    db.init_app(app)
    print("DB inicializado")


    login_manager.init_app(app)
    print("Login manager inicializado")

    login_manager.login_view = "usuario.login"

    with app.app_context():
        from .models import User, Task

        db.create_all()
        print("Tabelas criadas")


    from .routes import usuario
    from .routes import tasks

    app.register_blueprint(usuario)
    app.register_blueprint(tasks)

    return app
