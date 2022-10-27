from flask import redirect, render_template, request
from dojos_ninjas_app import app
from dojos_ninjas_app.models.model_dojo import Dojo
from dojos_ninjas_app.models.model_ninja import Ninja

@app.route("/dojos", methods=['GET','POST'])
def index():
    if request.method == 'GET':
        dojos = Dojo.get_all_dojos()
        return render_template("index.html",dojos=dojos)
    if request.method == 'POST':
        dojo = {
            "name":request.form['name']
        }
        dojo_created = Dojo.create_dojo(dojo)
        print("new dojo created id: ", dojo_created)
        return redirect('/dojos')

@app.route("/ninjas", methods=['GET','POST'])
def ninjas():
    if request.method == 'GET':
        dojos = Dojo.get_all_dojos()
        return render_template("ninjas.html",dojos=dojos)
    if request.method == 'POST':
        data={
            "first_name":request.form["first_name"],
            "last_name":request.form["last_name"],
            "age":request.form["age"],
            "dojo_id":request.form["id"],
        }
        response_query=Ninja.create_ninja(data)
        print("respuesta: ", response_query)
        return redirect('/dojos')

@app.route("/dojos/<number>", methods=['GET'])
def all_ninjas_dojo(number):
    data = {
        "id":number
    }
    dojo_name = ''
    response_query = Dojo.get_all_ninjas_dojo(data)
    dojos = Dojo.get_all_dojos()
    for dojo in dojos:
        if dojo.id==int(number):
            dojo_name=dojo.name
    return render_template("dojos.html", ninjas=response_query, dojo_name=dojo_name)