import os
from dotenv import load_dotenv

load_dotenv()

class Config():
    # Configurações do Banco de Dados
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Configurações dos Cookies e da sessões
    SESSION_COOKIE_SECURE = True
    PERMANENT_SESSION_LIFETIME = 3600
    # Configurações de formulários - Proteção CSRF
    WTF_CSRF_SECRET_KEY = os.getenv("WTF_CSRF_SECRET_KEY")
    WTF_CSRF_ENABLED = True
    WTF_CSRF_TIME_LIMIT = None
<<<<<<< HEAD


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    SESSION_COOKIE_SECURE = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
=======
>>>>>>> caa7929 (Gerenciador_tarefas)
