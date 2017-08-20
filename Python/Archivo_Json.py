__author__ = "Brayan Aroche"
import json
from ListaSimple import ListaSimple
listaS = ListaSimple()
#listaLocal = ListaSimple()

class Archivo_Json():
	def __init__(self):
		self.ruta_archivo = None

	def Lectura(self, path):
		contador = 0
		with open(path) as data_file:
			data=json.load(data_file)
			for key,value in data.iteritems():
				print key		
				for key1,value1 in value.iteritems():					
					#print key1
					#print value1
					if key1 == 'local':				
						#for i in value1:
						#print 'Local: '+ value1
						listaS.insertar("\""+value1+"\"")
					#if key1 == 'mascara':				
						#for i in value1:
						#print 'Mascara: '+value1
					if key1 == 'nodo':

						for i in value1:
							contador = contador + 1
							#prueba = "Nodo"
							#Nodo = "Nodo \""+contador+"\""
							#IP = i["ip"]
							#Carnet = i["carnet"]
							listaS.insertar("Nodo "+str(contador))
							listaS.insertar("\""+i["ip"]+"\"")
							listaS.insertar(i["carnet"])							
							#listaS.GenerarGrafico()					
							#Nodo_L = 'Nodo',contador
							#print 'Nodo',contador
							#IP = i["ip"]
							#print 'IP: '+ i["ip"]
							#Carnet = i["carnet"]
							#print 'Carne: '+ i["carnet"]
		listaS.GenerarGrafico()
		listaS.RecorridoListaSimple()

					