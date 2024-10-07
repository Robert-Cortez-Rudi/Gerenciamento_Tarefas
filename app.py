from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 


app = Flask(__name__)

@app.route("/")
def principal():
    return render_template("index.html")

# TERMINAR


if __name__ == "__main__":
    app.run(debug=True)
