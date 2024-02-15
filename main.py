from flask import Flask,render_template,request

import forms

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alumnos", methods = ["GET","POST"])
def alumnos():
    alumno_clase = forms.UserForm(request.form)
    
    nom = None
    apa = None
    ama = None
    edad = None
    email = None
    
    
    if request.method == "POST" and alumno_clase.validate():
        nom = alumno_clase.nombre.data
        apa = alumno_clase.apaterno.data
        ama = alumno_clase.amaterno.data
        edad = alumno_clase.edad.data
        email = alumno_clase.email.data
        
        print("Nombre: ".format(nom))
        print("Apellido Paterno: ".format(apa))
        print("Apellido Materno: ".format(ama))
        print("Email: ".format(email))
        print("Edad: ".format(edad))
    
    return render_template("alumnos.html", form = alumno_clase, nom = nom, apa = apa, ama = ama, email = email,edad = edad)

@app.route("/maestros")
def maestros():
    return render_template("maestros.html")
    
@app.route("/hola")
def hola():
    return "<h1>Saludo desde hola pai</h1>"

@app.route("/Saludo")
def saludo():
    return "<h1>Hola desde saludo</h1>"
    

@app.route("/nombre/<string:nom>")
def nombre(nom):
        return "<h1>Yooooo wasap " + nom
    
@app.route("/numero/<int:n1>")
def numero(n1):
    return "Numero: {}".format(n1)

@app.route("/user/<int:id>/<string:nom>")
def func(id,nom):
    return "ID: {} Nombre: {}".format(id,nom)

@app.route("/suma/<float:n1>/<float:n2>")
def func2(n1,n2):
    return "La suma {} + {} = {}".format(n1,n2,(n1+n2))

@app.route("/default")
@app.route("/default/<string:d>")
def func3(d="Dario"):
    return "El nombre de User es: " + d
    
@app.route("/calcular",methods=["GET","POST"])
def calcular():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "La multiplicacion de {} X {} = {}".format(num1,num2,str(int(num1)*int(num2)))
    else:
        return '''
                <form action="/calcular" method="POST">
                    <label>N1: </label>
                    <input class="form-control" type="text" name="n1"/><br>
                    <label>N2: </label>
                    <input class="form-control" type="text" name="n2"/><br>
                    <button class="btn btn-primary" type="submit">Enviar</button>
                </form>
                '''    
    
@app.route("/OperasBas")
def operas():
    return render_template("OperasBas.html") 

@app.route("/resultado",methods=["GET","POST"])
def resul():   
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "La multiplicacion de {} X {} = {}".format(num1,num2,str(int(num1)*int(num2)))
    
    
if __name__ == "__main__":
    app.run(debug=True)