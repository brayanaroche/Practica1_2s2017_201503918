class ListaDoble():

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def vacia(self):
        return self.primero == None
    
    def getValorNodo(self,index):
        contador = 0
        temp = self.primero
        while contador<index:
            temp = temp.siguiente
            contador +=1
        print temp.dato
        return temp.dato
    
    def getNodo(self,index):
        contador = 0
        temp = self.primero
        while contador<index:
            temp = temp.siguiente
            contador +=1
            
        return temp    
    
    def contains(self, obj):
        existe = False
        temp = self.primero
        
        for i in range(self.size):
            if temp.dato == obj:
                print("encontrado")
                existe = True
                break
            else:
                temp = temp.siguiente
                         
        return existe
    
    def getIndexOf(self, obj):
        index = 0
        temp = self.primero
        
        for i in range(self.size):
            if temp.dato == obj:
                print("encontrado")
                break
            else:
                temp = temp.siguiente
                index += 1                
                
        return index
        
    def addPrimero(self,dato):
        if self.vacia():
            self.primero = Nodo(dato)
            self.size += 1
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
            self.size += 1

    def removeInicio(self):
        if self.vacia():
            print("Esta Vacia")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size = 0
        else:
            self.primero = self.primero.siguiente
            self.primero.anterior = None
            self.size -= 1

    def recorrer_inicio(self):
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente
            
    def imprimirString(self):
        aux = self.primero
        string = ""
        while aux:
            string += str(aux.dato) + " -> "
            aux = aux.siguiente             
        return string   

    def Size(self):
        return self.size
    
    def removeAt(self, index):
        if index == 0:
            self.primero = self.primero.siguiente
        else:
            contador = 0
            temp = self.primero
            while contador < index -1:
                temp = temp.siguiente
                contador += 1
            temp.siguiente = temp.siguiente.siguiente
            
        self.size -= 1
