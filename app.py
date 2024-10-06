from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def principal():
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)
