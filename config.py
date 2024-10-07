import os
from dotenv import load_dotenv

load_dotenv()

class Config():
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_SECURE = True
    PERMANENT_SESSION_LIFETIME = 3600


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True # Exibe consultas SQL no console

# TERMINAR...

