col = cola.listaCola()
		colaMen = colaMensaje.listaColaMensaje()

		archivo = open(cadena, "r") 
		cadena= archivo.read()
		xmldoc = minidom.parseString(cadena)
		itemlist = xmldoc.getElementsByTagName("IP")
		for i in itemlist:
		    print ("ip= "+i.firstChild.nodeValue.strip())
		    col.add(i.firstChild.nodeValue.strip())
		itemlist = xmldoc.getElementsByTagName("texto")
		for i in itemlist:
		    print ("texto= "+i.firstChild.nodeValue.strip())
		    colaMen.add(i.firstChild.nodeValue.strip())
		colaMen.recorrer()
		col.recorrer()

cadena= archivo.read()
		xmldoc = minidom.parseString(cadena)
		itemlist = xmldoc.getElementsByTagName("IP")
		for i in itemlist:
		    print ("ip= "+i.firstChild.nodeValue.strip())
		    col.add(i.firstChild.nodeValue.strip())
		itemlist = xmldoc.getElementsByTagName("texto")
		for i in itemlist:
		    print ("texto= "+i.firstChild.nodeValue.strip())
		    colaMen.add(i.firstChild.nodeValue.strip())