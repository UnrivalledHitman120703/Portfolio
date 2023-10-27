# Python Flask file to handle the backend
# Name - Indrajeet Mondal; Date = 25th October 2023
# SourceCode

from flask import Flask, render_template

app = Flask(__name__)


# A normal routing
@app.route("/")
def my_():
    return render_template("index.html")



