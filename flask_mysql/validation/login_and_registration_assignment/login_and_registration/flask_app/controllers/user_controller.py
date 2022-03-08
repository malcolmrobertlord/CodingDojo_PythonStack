from dataclasses import dataclass
from flask_app import app
from flask import render_template, request, redirect, session, flash
# import the class from user.py
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

# ===================================
# route for creating user
# ===================================

@app.route("/create_user", methods = ["POST"])
def create_user():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password1'])
    print (pw_hash)
    
    data = {
        "first_name" : request.form["fname"],
        "last_name" : request.form["lname"],
        "email" : request.form["email"],
        "password" : pw_hash
    }
    user_id = User.save_user(data)
    session['user_id'] = user_id
    return redirect("/user")

# ===================================
# route for logging user in
# ===================================
@app.route("/login", methods = ["POST"])
def login_user():
    data = {
        "email" : request.form['email']
    }
    user_in_db = User.one_email(data)
    print(user_in_db)
    if not User.one_email(data):
        flash("Email/password incorrect")
        return redirect('/')
    
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Email/password incorrect")
        return redirect('/')
    
    session['user_id'] = user_in_db.id
    return redirect("/user")

# ===================================
# route for showing user dashboard
# ===================================
@app.route("/user")
def welcome_user():
    data = {
        "id" : session['user_id']
    }
    user = User.one_user(data)
    return render_template("welcome_user.html", user = user)
    return render_template("welcome_user.html")
    
# ===================================
# route for destroying session 
# ===================================

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect("/")