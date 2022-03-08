from flask_app import app
from flask import render_template, request, redirect
# import the class from friend.py
from flask_app.models.friend import Friend

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    return render_template("index.html", all_friends=friends)

# ===============================
# show one friend route
# ===============================

@app.route("/one_friend/<int:friend_id>")
def show_friend(friend_id):
    data = {
        "id" : friend_id
    }
    friend = Friend.one_friend(data)
    return render_template("show_one.html", friend=friend)


# ===============================
# Add friend route
# ===============================

@app.route("/new_friend")
def new_friend():
    return render_template("new_friend.html")

@app.route("/create_friend", methods = ["POST"])
def create_friend():
    data = {
        "first_name" : request.form["fname"],
        "last_name" : request.form["lname"],
        "age" : request.form["age"]
    }
    friend_id = Friend.save_friend(data)
    return redirect (f"/one_friend/{friend_id}")
