from config import MOVIMIENTOS_FILE, NEW_FILE, LAST_ID_FILE
import csv
import os

def select_all():
    """
    Devolverá una lista con todos los registros del fichero
    MOVIMIENTOS_FILE
    """
    fichero = open(MOVIMIENTOS_FILE, "r")

    csvReader = csv.reader(fichero, delimiter=',', quotechar='"')
    movimientos = []
    for movimiento in csvReader:
        movimientos.append(movimiento)

    # movimientos = [movimiento for movimiento in csvReader] #list comprehension

    fichero.close()
    return movimientos

def select_by(id):
    """
    Devolverá un registro con el id de la entrada o vacío si no lo encuentra
    MOVIMIENTOS_FILE
    """
    fichero = open(MOVIMIENTOS_FILE, "r", newline="")
    csvReader = csv.reader(fichero, delimiter=',', quotechar='"')
    registro_definitivo = []
    for registro in csvReader:
        if registro[0] == str(id):
            registro_definitivo = registro
            break

    fichero.close()

    return registro_definitivo

def delete_by(id):
    """
    Borrará el registro cuyo id coincide con el de la entrada
    MOVIMIENTOS_FILE
    """
    fichero_old = open(MOVIMIENTOS_FILE, "r")
    fichero = open(NEW_FILE, "w", newline="")
    csvReader = csv.reader(fichero_old, delimiter=",", quotechar='"')
    csvWriter = csv.writer(fichero, delimiter=",", quotechar='"')

    for registro in csvReader:
        if registro[0] != str(id):
            csvWriter.writerow(registro)

    fichero_old.close()
    fichero.close()

    os.remove(MOVIMIENTOS_FILE)
    os.rename(NEW_FILE, MOVIMIENTOS_FILE)

def createId():
    fichero = open(LAST_ID_FILE, "r")
    registro = fichero.read()
    id = int(registro) + 1
    fichero.close()
    return id

def saveLastId(id):
    fichero = open(LAST_ID_FILE, "w")
    fichero.write(f"{id}")
    fichero.close()           

def insert(registro):
    """
    Creará un nuevo registro, siempre y cuando registro sea compatible con el fichero. Asignará
    al registro un id único (acumulativo)
    MOVIMIENTOS_FILE
    """
    id = createId()

    fichero = open(MOVIMIENTOS_FILE, "a", newline="")
    csvWriter = csv.writer(fichero, delimiter=",", quotechar='"')

    #csvWriter.writerow(["{}".format(id), registro[0], registro[1], registro[2]])
    csvWriter.writerow([f"{id}"]+registro)
    fichero.close()

    saveLastId(id)


def update_by(registro_mod):
    """
    Sobreescribirá el registro cuyo id coincide con el de entrada
    """
    fichero_old = open(MOVIMIENTOS_FILE, "r")
    fichero = open(NEW_FILE, "w", newline="")
    csvReader = csv.reader(fichero_old, delimiter=",", quotechar='"')
    csvWriter = csv.writer(fichero, delimiter=",", quotechar='"')

    for registro in csvReader:
        if registro[0] != registro_mod[0]:
            csvWriter.writerow(registro)
        else:
            csvWriter.writerow(registro_mod)

    fichero_old.close()
    fichero.close()

    os.remove(MOVIMIENTOS_FILE)
    os.rename(NEW_FILE, MOVIMIENTOS_FILE)