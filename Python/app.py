import json
from Pila import Pila
from pprint import pprint

with open("C:\Users\Aroche\Documents\Cursos Usac\EDD\Practica 1\Practica1 EDD\Archivo1.json") as data_file:
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
					
	#pprint(data["nodos"]["nodo"][1]["ip"])