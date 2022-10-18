from nodo import Nodo
from arista import Arista, AristaNoDirigida
from grafo import Grafo

def busquedaAnchura(ListaAdyacencia: dict, nodoInicial):
   noNodos= len(ListaAdyacencia)
   nodosAbiertos= []
   nodosCerrados= []

   def expandirNodos(nodoActual):
      for i in range(len(ListaAdyacencia[nodoActual])):
         if ListaAdyacencia[nodoActual][i][0] in nodosAbiertos or ListaAdyacencia[nodoActual][i][0] in nodosCerrados:
           pass
         else: 
           nodosAbiertos.append(ListaAdyacencia[nodoActual][i][0])
        
   nodosAbiertos.append(nodoInicial)
   while len(nodosCerrados) != noNodos:
      nodoActual= nodosAbiertos[0]

      expandirNodos(nodoActual)
      nodosCerrados.append(nodoActual)
      nodosAbiertos.pop(nodosAbiertos.index(nodoActual))
    
   # print(nodosAbiertos)
   print(nodosCerrados, "\n")

def busquedaProfundidad(ListaAdyacencia: dict, nodoInicial, arbol):
   noNodos= len(ListaAdyacencia)
   nodosAbiertos= []
   nodosCerrados= []

   def expandirNodos(nodoActual):
      noNodosAdyacentes= len(ListaAdyacencia[nodoActual])-1
      for i in range(noNodosAdyacentes+1):
         if ListaAdyacencia[nodoActual][noNodosAdyacentes-i][0] in nodosAbiertos or ListaAdyacencia[nodoActual][noNodosAdyacentes-i][0] in nodosCerrados:
           pass
         else: 
           nodosAbiertos.append(ListaAdyacencia[nodoActual][noNodosAdyacentes-i][0])
        
   def adyacencia(nodoActual):
      adyacente= False
      for i in range(len(ListaAdyacencia[nodosCerrados[len(nodosCerrados)-1]])):
         if nodoActual == ListaAdyacencia[nodosCerrados[len(nodosCerrados)-1]][i][0]:
           adyacente= True

      return adyacente

   expandirNodos(nodoInicial)
   nodosCerrados.append(nodoInicial)
   while len(nodosCerrados) != noNodos:
      noNodosAbiertos= len(nodosAbiertos)
      if arbol == True: 
        nodoActual= nodosAbiertos[noNodosAbiertos-1]
      
      if arbol == False:
        nodosAbiertos.sort(reverse= True)
        for i in range(noNodosAbiertos):
           nodoActual= nodosAbiertos[(noNodosAbiertos-i)-1]
           if adyacencia(nodoActual):
             break

      expandirNodos(nodoActual)
      nodosCerrados.append(nodoActual)
      nodosAbiertos.pop(nodosAbiertos.index(nodoActual))
    
   # print(nodosAbiertos)
   print(nodosCerrados, "\n")

def primeroMejor(ListaAdyacencia: dict, nodoInicial, nodoFinal):
   noNodos= len(ListaAdyacencia)
   nodosAbiertos= []
   nodosCerrados= []

   def heuristica():
      valores= []
      # Los agregamos de forma manual como ejemplo
      # Despues se puede modificar la funcion
      valores.append(0) # Nodo 1
      valores.append(4)
      valores.append(1)
      valores.append(7)
      valores.append(1)
      valores.append(7)
      valores.append(2)
      valores.append(6)
      valores.append(1)
      valores.append(2)
      valores.append(5)
      valores.append(3)
      valores.append(10)
      valores.append(7)
      valores.append(6)
      valores.append(9)
      valores.append(5)
      valores.append(8)
      valores.append(15)
      valores.append(0) # Nodo 20

      return valores

   def nodoAbierto(nodoActual):
      for i in range(len(nodosAbiertos)):
          if nodoActual == nodosAbiertos[i][0]:
            return True
 
   def nodoCerrado(nodoActual):
      for i in range(len(nodosCerrados)):
          if nodoActual == nodosCerrados[i][0]:
            return True

   def expandirNodos(nodoActual):
       aux= []
       noNodosAdy= len(ListaAdyacencia[nodoActual])
       for i in range(noNodosAdy):
          if nodoAbierto(ListaAdyacencia[nodoActual][i][0]) or nodoCerrado(ListaAdyacencia[nodoActual][i][0]):
            pass
          else: 
            aux.append([ListaAdyacencia[nodoActual][i][0], valoresHeuristica[ListaAdyacencia[nodoActual][i][0]-1]])
            aux.sort(reverse= True, key=lambda aux : aux[1])

       for i in range(len(aux)):
          nodosAbiertos.append(aux[i])
   
   valoresHeuristica= heuristica()
   # print(valoresHeuristica)

   nodosCerrados.append([nodoInicial, valoresHeuristica[nodoInicial-1]])
   expandirNodos(nodoInicial)
   nodoDestino= False
   while nodoDestino == False:
      noNodosAbiertos= len(nodosAbiertos)
      nodoActual= nodosAbiertos[noNodosAbiertos-1][0]
      if nodoActual == nodoFinal:
        nodosCerrados.append(nodosAbiertos[noNodosAbiertos-1])
        nodosAbiertos.pop(noNodosAbiertos-1)
        nodoDestino= True
      else:
        nodosCerrados.append(nodosAbiertos[noNodosAbiertos-1])
        nodosAbiertos.pop(noNodosAbiertos-1)
        expandirNodos(nodoActual)

   #print(nodosAbiertos)
   #print(nodosCerrados)

   camino= []
   for i in range(len(nodosCerrados)):
      camino.append(nodosCerrados[i][0])

   print(camino)

# Creamos el grafo

# Arista no dirigida
# arista1= AristaNoDirigida(Nodo(1), Nodo(3), 0)
# arista2= AristaNoDirigida(Nodo(1), Nodo(6), 0)
# arista3= AristaNoDirigida(Nodo(3), Nodo(2), 0)
# arista4= AristaNoDirigida(Nodo(3), Nodo(6), 0)
# arista5= AristaNoDirigida(Nodo(3), Nodo(5), 0)
# arista6= AristaNoDirigida(Nodo(6), Nodo(5), 0)
# arista7= AristaNoDirigida(Nodo(6), Nodo(7), 0)
# arista8= AristaNoDirigida(Nodo(2), Nodo(5), 0)
# arista9= AristaNoDirigida(Nodo(2), Nodo(4), 0)
# arista10= AristaNoDirigida(Nodo(5), Nodo(7), 0)
# arista11= AristaNoDirigida(Nodo(5), Nodo(4), 0)
# arista12= AristaNoDirigida(Nodo(7), Nodo(4), 0)

# arista1= AristaNoDirigida(Nodo('A'), Nodo('C'), 0)
# arista2= AristaNoDirigida(Nodo('A'), Nodo('F'), 0)
# arista3= AristaNoDirigida(Nodo('C'), Nodo('B'), 0)
# arista4= AristaNoDirigida(Nodo('C'), Nodo('F'), 0)
# arista5= AristaNoDirigida(Nodo('C'), Nodo('E'), 0)
# arista6= AristaNoDirigida(Nodo('F'), Nodo('E'), 0)
# arista7= AristaNoDirigida(Nodo('F'), Nodo('G'), 0)
# arista8= AristaNoDirigida(Nodo('B'), Nodo('E'), 0)
# arista9= AristaNoDirigida(Nodo('B'), Nodo('D'), 0)
# arista10= AristaNoDirigida(Nodo('E'), Nodo('G'), 0)
# arista11= AristaNoDirigida(Nodo('E'), Nodo('D'), 0)
# arista12= AristaNoDirigida(Nodo('G'), Nodo('D'), 0)

# Grafo
# grafo= Grafo()
# grafo.agregarArista(arista1)
# grafo.agregarArista(arista2)
# grafo.agregarArista(arista3)
# grafo.agregarArista(arista4)
# grafo.agregarArista(arista5)
# grafo.agregarArista(arista6)
# grafo.agregarArista(arista7)
# grafo.agregarArista(arista8)
# grafo.agregarArista(arista9)
# grafo.agregarArista(arista10)
# grafo.agregarArista(arista11)
# grafo.agregarArista(arista12)
# print(grafo)
# -------------------------------------------------------------

# Creamos arbol como ejemplo
arista1= AristaNoDirigida(Nodo(1), Nodo(2), 0)
arista2= AristaNoDirigida(Nodo(1), Nodo(3), 0)
arista3= AristaNoDirigida(Nodo(1), Nodo(4), 0)
arista4= AristaNoDirigida(Nodo(2), Nodo(5), 0)
arista5= AristaNoDirigida(Nodo(2), Nodo(6), 0)
arista6= AristaNoDirigida(Nodo(4), Nodo(7), 0)
arista7= AristaNoDirigida(Nodo(4), Nodo(8), 0)
arista8= AristaNoDirigida(Nodo(4), Nodo(9), 0)
arista9= AristaNoDirigida(Nodo(6), Nodo(10), 0)
arista10= AristaNoDirigida(Nodo(6), Nodo(11), 0)
arista11= AristaNoDirigida(Nodo(7), Nodo(12), 0)
arista12= AristaNoDirigida(Nodo(7), Nodo(13), 0)
arista13= AristaNoDirigida(Nodo(9), Nodo(14), 0)
arista14= AristaNoDirigida(Nodo(9), Nodo(15), 0)
arista15= AristaNoDirigida(Nodo(9), Nodo(16), 0)
arista16= AristaNoDirigida(Nodo(11), Nodo(17), 0)
arista17= AristaNoDirigida(Nodo(11), Nodo(18), 0)
arista18= AristaNoDirigida(Nodo(13), Nodo(19), 0)
arista19= AristaNoDirigida(Nodo(13), Nodo(20), 0)

# Arbol
grafo= Grafo()
grafo.agregarArista(arista1)
grafo.agregarArista(arista2)
grafo.agregarArista(arista3)
grafo.agregarArista(arista4)
grafo.agregarArista(arista5)
grafo.agregarArista(arista6)
grafo.agregarArista(arista7)
grafo.agregarArista(arista8)
grafo.agregarArista(arista9)
grafo.agregarArista(arista10)
grafo.agregarArista(arista11)
grafo.agregarArista(arista12)
grafo.agregarArista(arista13)
grafo.agregarArista(arista14)
grafo.agregarArista(arista15)
grafo.agregarArista(arista16)
grafo.agregarArista(arista17)
grafo.agregarArista(arista18)
grafo.agregarArista(arista19)
# print(grafo)

ListaAdyacencia= grafo.getListaAdyacencia()
# print(ListaAdyacencia, "\n")

# Algoritmos
print("Busqueda en Anchura")
busquedaAnchura(ListaAdyacencia, 1)

print("Busqueda en Profundidad")
# busquedaProfundidad(ListaAdyacencia, 7, arbol= False)
busquedaProfundidad(ListaAdyacencia, 1, arbol= True)

print("Primero el mejor")
primeroMejor(ListaAdyacencia, 1, 20)
