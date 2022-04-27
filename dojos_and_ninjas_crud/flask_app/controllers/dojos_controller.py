from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.dojos import Dojos

@app.route("/")
def index():
    dojos = Dojos.get_all()
    return render_template("dojos.html", dojos = dojos)

@app.route("/dojos/create/", methods = ["POST"])
def new_dojo():
    data = {
        "name": request.form["dojo_name"]
    }
    new_dojo_id = Dojos.new_dojo(data)

    return redirect("/")


@app.route("/dojos/<int:dojo_id>")
def show_one_dojo(dojo_id):
    print("==============")
    print(dojo_id)
    data = {
        "id" : dojo_id
    }
    print(data)

    one_dojo = Dojos.get_dojos_friends(data)
    print(one_dojo)
    return render_template("dojo_ninjas.html", one_dojo = one_dojo)
