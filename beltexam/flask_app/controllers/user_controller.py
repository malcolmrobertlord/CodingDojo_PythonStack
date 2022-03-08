from crypt import methods
from flask_app import app
from flask import render_template, request, redirect, session, flash
# import the class from user.py
from flask_app.models.user import User
from flask_app.models.show import Show
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# ===================================
#Landing Page for login/registration
# ===================================
@app.route("/")
def log_reg():
    return render_template("log_reg.html")

# ===================================
# Processing Registration
# ===================================
@app.route("/register", methods=["POST"])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print (pw_hash)
    data = {
        "first_name" : request.form["fname"],
        "last_name" : request.form["lname"],
        "email" : request.form["email"],
        "password" : pw_hash
    }
    user_id = User.save_user(data)
    session['user_id'] = user_id
    return redirect("/dashboard")

# ===================================
# Login route
# ===================================

@app.route("/login", methods=['POST'])
def login():
    data = {
        "email" : request.form['email']
    }
    user_in_db = User.one_email(data)
    print(user_in_db)
    if not user_in_db:
        flash("Email/password incorrect")
        return redirect('/')
    
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Email/password incorrect")
        return redirect('/')
    
    session['user_id'] = user_in_db.id
    return redirect("/dashboard")

# ===================================
# route for destroying session 
# ===================================

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect("/")