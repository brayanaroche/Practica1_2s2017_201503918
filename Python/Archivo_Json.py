__author__ = "Brayan Aroche"
import json
from ListaSimple import ListaSimple

class Archivo_Json():
	def __init__(self):
		self.ruta_archivo = None
		

	def Lectura(self, path):
		with open(path) as data_file:
			data=json.load(data_file)
			for key,value in data.iteritems():
				print key		
				for key1,value1 in value.iteritems():					
					#print key1
					#print value1
					if key1 == 'local':				
						#for i in value1:
						print 'Local: '+value1
					if key1 == 'mascara':				
						#for i in value1:
						print 'Mascara: '+value1
					if key1 == 'nodo':				
						for i in value1:
							print 'IP: '+ i["ip"]
							print 'Carne: '+ i["carnet"]
							print 'Mascara: '+ i["mascara"]			
					