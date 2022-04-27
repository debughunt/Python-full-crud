from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User

@app.route("/")
def index():
    users = User.get_all()
    return render_template("allUsers.html", users = users)


@app.route("/createUser/")
def user_form():
    return render_template("createUser.html")


@app.route("/createNew/", methods = ["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    new_user_id = User.new_user(data)

    return redirect("/")

@app.route("/user/<int:user_id>")
def get_one(user_id):
    query_data = {
        "user_id" : user_id
    }
    one_user = User.get_one(query_data)
    return render_template("profile.html", one_user = one_user)


@app.route("/edit/<int:user_id>")
def edit(user_id):
    query_data = {
        "user_id" : user_id
    }
    user = User.get_one(query_data)
    return render_template("editProf.html", user = user)

@app.route("/editProf/<int:user_id>", methods = ["POST"])
def edit_prof(user_id):
    query_data = {
        "user_id" : user_id,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.edit_user(query_data)
    return redirect(f"/user/{user_id}")

@app.route("/delete/<int:user_id>")
def delete_user(user_id):
    query_data = {
        "user_id" : user_id
    }
    User.delete_user(query_data)
    return redirect("/")