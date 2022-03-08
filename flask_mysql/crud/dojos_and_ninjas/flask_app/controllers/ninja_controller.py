from flask_app import app
from flask import render_template, request, redirect
# import the class from user.py
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/new_ninja")
def new_ninja():
    all_dojos = Dojo.get_all()
    return render_template("new_ninja.html", dojos=all_dojos)

@app.route("/create_ninja", methods = ["POST"])
def create_ninja():
    data = {
        "first_name" : request.form["fname"],
        "last_name" : request.form["lname"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo_id"],
    }
    dojo_id = request.form["dojo_id"]
    Ninja.save_ninja(data)
    return redirect((f"/dojo/{dojo_id}"))