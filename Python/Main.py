from Pila import Pila
from Cola import Cola
#from ListaDoble import ListaDoble
from ListaSimple import ListaSimple
from Archivo_Json import Archivo_Json

#Variables para el llamar a otros metodos o funcioes dentro de la clase pila, cola, lista doble o simple
pila = Pila()
cola = Cola()
#listaD = ListaDoble
listaS = ListaSimple()
arjson = Archivo_Json()

#Importando flask para nuestro servidor
from flask import Flask, request, Response

app = Flask("Practica1")
#Metodo para Pila
@app.route('/ArchivoJson',methods = ['POST'])
def AbrirArchivo():
	#ruta = str(request.form["ruta"])
	#parametro = request.args.get(ruta,'No contiene ruta')
	parametro = str(request.form["ruta"])
	arjson.Lectura(parametro)	
	return "C:\graficas\Reporte.html"

@app.route('/hola', methods =['GET'])
def index():
	listaS.insertar(1)
	listaS.insertar(2)
	listaS.GenerarGrafico()

	return "Hello World Brayan aroche"

if __name__ == "__main__":
  app.run(debug=True, host='127.0.0.1')





