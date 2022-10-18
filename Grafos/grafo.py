from nodo import Nodo
from arista import Arista

class Grafo:
    def __init__(self) -> None:
        self.__aristas= []
        self.__adyacencia= dict() # {}

    def agregarArista(self, arista: Arista):
        if arista not in self.__aristas:
          self.__aristas.append(arista)

    def eliminarArista(self, arista: Arista):
        self.__aristas.remove(arista)

    def agregarAdyacencia(self, dato1, dato2, peso):
        if dato1 in self.__adyacencia:
          self.__adyacencia[dato1].append([dato2, peso])
        else:
          self.__adyacencia[dato1]= [[dato2, peso]]

    def getListaAdyacencia(self):
        for arista in self.__aristas:
           if arista.dirigido():
             pass
           else:
             nodo1= arista.getNodo1()
             nodo2= arista.getNodo2()
             peso= arista.getPeso()

             self.agregarAdyacencia(nodo1.dato, nodo2.dato, peso)
             self.agregarAdyacencia(nodo2.dato, nodo1.dato, peso)
        
        for key in self.__adyacencia:
          self.__adyacencia[key].sort()

        return self.__adyacencia

    def __str__(self) -> str:
        return str([str(arista) for arista in self.__aristas])


    