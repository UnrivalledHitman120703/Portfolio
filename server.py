# Python Flask file to handle the backend
# Name - Indrajeet Mondal; Date = 25th October 2023
# SourceCode

from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


# index.html routing
@app.route("/index.html")
def home():
    return render_template("index.html")


# about.html routing
@app.route("/about.html")
def about():
    return render_template("about.html")


# work.html routing
@app.route("/works.html")
def work():
    return render_template("works.html")


# contact.html routing
@app.route("/contact.html")
def contact():
    return render_template("contact.html")


# components.html routing
@app.route("/components.html")
def components():
    return render_template("components.html")

# writing data to database.csv
def write_to_file(data):
    with open("database.csv", mode="a", newline="") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            database,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL,
        )
        csv_writer.writerow([email, subject, message])


# Dynamic page loading
@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


# Submit a contact form
@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_file(data)
        return redirect("/thankyou.html")
    else:
        return "Something went wrong !!"
