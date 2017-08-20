from xml.dom import minidom
xmldoc = minidom.parse('ArchivoXML.xml')
itemlist = xmldoc.getElementsByTagName('nodos')
print(len(itemlist))
print(itemlist[0].attributes['name'].value)
for s in itemlist:
    print(s.attributes['name'].value)