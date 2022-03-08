from flask_app import app
from flask import render_template, request, redirect
# import the class from user.py
from flask_app.models.user import User

@app.route("/users")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    return render_template("read_all.html", all_users=users)

# ===============================
# show one user route
# ===============================

@app.route("/one_user/<int:user_id>")
def show_user(user_id):
    data = {
        "id" : user_id
    }
    user = User.one_user(data)
    return render_template("show_one.html", user=user)


# ===============================
# Add user route
# ===============================

@app.route("/new_user")
def new_user():
    return render_template("create.html")

@app.route("/create_user", methods = ["POST"])
def create_user():
    data = {
        "first_name" : request.form["fname"],
        "last_name" : request.form["lname"],
        "email" : request.form["email"]
    }
    user_id = User.save_user(data)
    return redirect ("/users")


# ===============================
# Edit user route
# ===============================

@app.route("/edit_user/<int:user_id>")
def edit_user(user_id):
    data = {
        "id" : user_id
    }
    user = User.one_user(data)
    return render_template("edit.html", user=user)

@app.route("/update_user", methods = ["POST"])
def update_user():
    data = {
        "id" : request.form["id"],
        "first_name" : request.form["fname"],
        "last_name" : request.form["lname"],
        "email" : request.form["email"]
    }
    user_id = User.edit_user(data)
    return redirect ("/users")

# ===============================
# Delete user route
# ===============================

@app.route("/delete_user/<int:user_id>")
def delete_user(user_id):
    return render_template("delete.html", user_id=user_id)

@app.route("/delete/<int:user_id>")
def delete(user_id):
    data = {
        "id" : user_id
    }
    User.delete_user(data)
    return redirect ("/users")