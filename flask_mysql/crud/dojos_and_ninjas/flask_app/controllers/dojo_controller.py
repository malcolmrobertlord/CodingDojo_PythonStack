from flask_app import app
from flask import render_template, request, redirect
# import the class from user.py
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/dojos")
def index():
    # call the get all classmethod to get all dojos
    dojos = Dojo.get_all()
    return render_template("dojos.html", all_dojos=dojos)

# ===============================
# Add dojo route
# ===============================

@app.route("/create_dojo", methods = ["POST"])
def create_dojo():
    data = {
        "name" : request.form["name"],
    }
    dojo_id = Dojo.save_dojo(data)
    return redirect ("/dojos")


# ===============================
# Show dojo's ninjas route
# ===============================

@app.route("/dojo/<dojo_id>")
def show_dojo(dojo_id):
    data = {
        "dojo_id" : dojo_id
    }
    one_dojo = Dojo.one_dojo(data)
    ninjas = Ninja.one_dojo_ninjas(data)
    return render_template ("dojo_ninjas.html", ninjas=ninjas, one_dojo=one_dojo)
