from flask_app import app
from flask import render_template, session, redirect, request

from flask_app.models.team import Team 
from flask_app.models.owner import Owner

# =================================================
# Create an Owner
    # Render the Form
@app.route("/makeOwner")
def makeOwner():
    return render_template("make_owner.html")

    # Process the Post
@app.route("/makingOwner", methods = ['POST'])
def making_owner():
    data = {
        "first_name" :request.form["first_name"],
        "last_name" :request.form["last_name"]
    }
    owner_id = Owner.save_owner(data)
    return redirect("/")
# =================================================

# =================================================
# View one owner
# ===========================================
@app.route("/owner/<int:owner_id>")
def show_owner(owner_id):
    data = {
        "id" : owner_id
    }
    owner = Owner.one_owner(data)
    return render_template("one_owner.html", owner = owner)


## =================================================
# Update owner
# =================================================


# =================================================
# Delete route
# ================================================= 
