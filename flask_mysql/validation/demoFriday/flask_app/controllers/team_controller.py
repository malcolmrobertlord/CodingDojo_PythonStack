from flask_app import app
from flask import render_template, session, redirect, request

from flask_app.models.team import Team 
from flask_app.models.owner import Owner


@app.route("/")
def index():
    if "user_id" in session:
        data = {
            "id" : session['user_id']
        }
        user = User.one_user(data)
        all_teams = Team.all_teams()
        all_owners = Owner.all_owners()
        return render_template("index.html", all_teams=all_teams, all_owners = all_owners, user = user)
    else:
        return render_template("login_registration.html")


# =================================================
# create a team

# route to render create form
@app.route("/make_team")
def make_team():
    return render_template("make_team.html")
    
# route to process POST
@app.route("/making_team", methods=['POST'])
def making_team():
    data = {
        "name" : request.form['name'],
        "location" : request.form['location'],
        "sport" : request.form['sport'],
        "champs" : request.form['champs']
    }
    Team.save_team(data)
    return redirect("/")
# =================================================

# =================================================
# delete a team
# =================================================

@app.route("/delete_team")
def delete_team():
    return redirect("/")

# =================================================
# update a team

# route to render create form
@app.route("/update_team")
def update_team():
    return render_template("update_team.html")
    
# route to process POST
@app.route("/updating_team")
def updating_team():
    
    return redirect("/")

# =================================================