from Pila import Pila
p = Pila()
print p.Vacia()
p.push(5)
p.push(57)
print p.Vacia()
p.push("Hola")
p.push(5)
p.pop()
p.imprimir()
p.push("Como estas")
p.push("Perro")
p.pop()
p.push("Si sale XD")
p.imprimir()
p.GenerarGrafico()