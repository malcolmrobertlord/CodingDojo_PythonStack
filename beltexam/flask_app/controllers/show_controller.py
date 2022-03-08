from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user import User
from flask_app.models.show import Show


# ===================================
# Dashboard route
# ===================================
@app.route("/dashboard")
def index():
    if not "user_id" in session:
        return render_template("log_reg.html")
    else:
        data = {
            "id" : session['user_id']
        }
        user = User.one_user(data)
        shows = Show.get_all_shows()
        return render_template("dashboard.html", user = user, all_shows = shows)
    
# ===================================
# Add a show route
# ===================================
@app.route("/add_show")
def new_user():
    if not "user_id" in session:
        return render_template("log_reg.html")
    else:
        data = {
            "id" : session['user_id']
        }
        user = User.one_user(data)
        return render_template("add_show.html", user=user)

@app.route("/create_show", methods = ["POST"])
def create_user():
    if not Show.validate_show(request.form):
        return redirect('/add_show')
    data = {
        "title" : request.form["title"],
        "network" : request.form["network"],
        "release_date" : request.form["release_date"],
        "description" : request.form["description"],
        "user_id" :request.form["user_id"]
    }
    show_id = Show.save_show(data)
    return redirect ("/dashboard")

# ===================================
# Display one show route
# ===================================
@app.route("/show_show/<show_id>")
def show_show(show_id):
    if not "user_id" in session:
        return render_template("log_reg.html")
    else:
        data = {
            "show_id" : show_id
        }
        show = Show.one_show(data)
        data2 = {
            "id" : show.user_id
        }
        user = User.one_user(data2)
        return render_template("show_show.html", show=show, user=user)
    
# ===================================
# Edit one show route
# ===================================
@app.route("/edit_show/<int:show_id>")
def edit_user(show_id):
    if not "user_id" in session:
        return render_template("log_reg.html")
    else:
        user_id = session['user_id']
        data = {
            "show_id" : show_id
        }
        show = Show.one_show(data)
        return render_template("edit_show.html", user_id=user_id, show=show)

@app.route("/update_show/<int:show_id>", methods = ["POST"])
def update_show(show_id):
    if not Show.validate_show(request.form):
        return redirect(f'/edit_show/{show_id}')
    data = {
        "title" : request.form["title"],
        "network" : request.form["network"],
        "release_date" : request.form["release_date"],
        "description" : request.form["description"],
        "id" : show_id
    }
    show_id = Show.edit_show(data)
    return redirect ("/dashboard")

# ===================================
# DELETE one show route
# ===================================

@app.route("/delete_show/<int:show_id>")
def delete_show(show_id):
    data = {
        "show_id" : show_id
    }
    show = Show.one_show(data)
    return render_template("delete_show.html", show=show)

@app.route("/delete/<int:show_id>")
def delete(show_id):
    data = {
        "id" : show_id
    }
    Show.delete_show(data)
    return redirect ("/dashboard")