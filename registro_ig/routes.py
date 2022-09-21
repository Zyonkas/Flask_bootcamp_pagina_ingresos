from crypt import methods
from flask import render_template, request, redirect
import csv
from registro_ig import app
from datetime import date


@app.route("/")
def index():
    fichero = open("data/movimientos.txt", "r")
    csvReader = csv.reader(fichero, delimiter=',', quotechar='"')
    movimientos = []
    for movimiento in csvReader:
        movimientos.append(movimiento)

    # movimientos = [movimiento for movimiento in csvReader] #list comprehension

    fichero.close()
    return render_template("index.html", pageTitle="Lista", movements=movimientos)

@app.route("/nuevo", methods=["GET", "POST"])
def alta():
    if request.method == "GET":
        return render_template("new.html", pageTitle="Alta", 
                               dataForm={})
    else:
        """
            1. Validar el formulario
                Fecha valida y <= hoy
            2. Concepto no sea vacío
            3. Cantidad no se cero     
        """
        errores = validaFormulario(request.form)

        if not errores:
            fichero = open("data/movimientos.txt", "a", newline="")
            csvWriter = csv.writer(fichero, delimiter=",", quotechar='"')

            # Generar un nuevo id

            csvWriter.writerow([request.form['date'], request.form['concept'], request.form['quantity']])
            fichero.close()

            return redirect("/")
        else:
            return render_template("new.html", pageTitle="Alta", msgErrors=errores, dataForm=dict(request.form))

def validaFormulario(camposFormulario):
    errores = []
    hoy = date.today().isoformat()
    if camposFormulario['date'] > hoy:
        errores.append("La fecha introducida es es futuro.")

    if camposFormulario['concept'] == "":
        errores.append("Introduce un concepto para la transacción.")

    #La primera condición es para que el número sea distinto de cero
    #la segunda condición es para que el campo no esté vacío
    if camposFormulario["quantity"] == "" or float(camposFormulario["quantity"]) == 0.0:
        errores.append("Introduce una cantidad positiva o negativa.")

    return errores

    
@app.route("/modificar/<int:id>", methods=["GET", "POST"])
def modifica(id):
    if request.method == "GET":
        """
        1. Consultar en movimientos.txt y recueperar el registro con id al de la petición
        2. Devolver el formulario html con los datos de mi registro
        """

        return render_template("modifica.html", registro=[])
    else:
        """
        1. validar registro de entrada
        2. Si el registro es correcto lo sustituyo en movimientos.txt. La mejor manera es copiar registro a registro e fichero nuevo y dar el cambiazo
        3. redirect 
        4. Si el registro es incorrecto la gestion de errores que conocemos
        """
        pass

@app.route("/borrar/<int:id>", methods=["GET", "POST"])
def borrar(id):
    if request.method == "GET":
        """
        1. Consultar en movimientos.txt y recueperar el registro con id al de la petición
        2. Devolver el formulario html con los datos de mi registro, no modificables 
        3. Tendrá un boton que diga confirmar.
        """
        return render_template("borra.html", registro=[])
    else:
        """
            Borrar el registro
        """       
        pass
         