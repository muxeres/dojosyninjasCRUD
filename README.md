# Dojos Ninjas

### Python - flask - mysql

### Install packages

* ``pipenv install PyMySQL flask``
* ``pipenv shell``
* ``python server.py``

### Inicio

* ``http://127.0.0.1:5000/dojos``

### Estructura

```
├── server.py
└── dojos_ninjas_app/
    ├── __init__.py
    ├── config/
    |   └── mysqlconnection.py
    ├── controllers/
    |   └── controler_dojos_ninjas.py
    ├── models/
    |   └── model_dojo.py
    |   └── model_ninja.py
    └── templates/
        ├── index.html
        ├── dojos.html
        └── ninjas.html
```

### Estructura Controllers  ``controller_dojos_ninjas.py``

| routs                             | Funtions                | return                                                                    | methods   |
| --------------------------------- | ----------------------- | ------------------------------------------------------------------------- | --------- |
| Localhost:5000/dojos              | index()                 | render_template("index.html",dojos=dojos),redirect("/dojos")              | GET, POST |
| Localhost:5000/ninjas             | ninjas()                | render_template("ninjas.html",dojos=dojos),return redirect('/dojos')      | GET, POST |
| Localhost:5000/dojos/`<number>` | all_ninjas_dojo(number) | render_template("dojos.html", ninjas=response_query, dojo_name=dojo_name) | GET       |
