from Pila import Pila
from Cola import Cola
#from ListaDoble import ListaDoble
from ListaSimple import ListaSimple

#Variables para el llamar a otros metodos o funcioes dentro de la clase pila, cola, lista doble o simple
pila = Pila()
cola = Cola()
#listaD = ListaDoble
listaS = ListaSimple

#Importando flask para nuestro servidor
from flask import Flask, request, Response

app = Flask("Practica1")

#Metodo post para lista simple
@app.route('/ListaSimple', methods = ['POST']) 
def lista():
	if str(request.form['tipo'])=="insertar":
		ls.insertar(str(request.form['informacion']))
		ls.GenerarGrafico()

	elif str(request.form['tipo'])=="eliminar":
		indice = int(request.form['informacion'])
		ls.eliminar(indice)
		ls.GenerarGrafico()

	elif str(request.form['tipo'])=="buscar":
		
		return str(ls.buscar(str(request.form['informacion']))) 


#Metodo para Cola
@app.route('/Cola',methods = ['POST'])
def cola4():
	if str(request.form['tipo'])=="insertar":
		cola.queque(request.form['informacion'])
		cola.GenerarGrafico()

	elif str(request.form['tipo'])=="eliminar":
		r = str(cola.dequeque())
		cola.GenerarGrafico()
		return r
		

#Metodo para Pila
@app.route('/Pila',methods = ['POST'])
def pila4():
	if str(request.form['tipo'])=="push":
		pila.push(str(request.form['informacion']))
		pila.GenerarGrafico()

	elif str(request.form['tipo'])=="pop":
		r = str(pila.pop())
		pila.GenerarGrafico()
		return r
		
@app.route('/hola')
def index():
	return "Hello World Brayan aroche"

if __name__ == "__main__":
  app.run(debug=True, host='127.0.0.1')





