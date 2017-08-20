__author__ = "Brayan Aroche"
import json
from pprint import pprint

class Archivo_Json():
	def __init__(self):
		self.ruta_archivo = None
		

	def Lectura(self, path):
		with open(path) as data_file:
			data=json.load(data_file)
			for key,value in data.iteritems():
				#print "Local"+key		
				for key1,value1 in value.iteritems():
					#print key1
					if key1 == 'nodo':				
						for i in value1:
							print i["ip"]
							print i["carnet"]
							print i["mascara"]			