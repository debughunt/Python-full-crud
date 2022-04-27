from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.ninjas import Ninjas
from flask_app.models.dojos import Dojos

@app.route("/ninjas/")
def new_ninjas():
    dojos = Dojos.get_all()
    return render_template("ninjas.html", dojos = dojos)



@app.route("/ninjas/create/", methods = ["POST"])
def create_ninja():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojos"]
    }
    new_ninja_id = Ninjas.new_ninja(data)
    return redirect("/")

