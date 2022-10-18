from nodo import Nodo

class Arista:
    def __init__(self, nodo1: Nodo, nodo2: Nodo, peso: int) -> None:
        self.__arista= [nodo1, nodo2, peso]

    def dirigido(self) -> bool:
        return False

    def ponderado(self) -> bool:
        return False

    def getArista(self) -> list:
        return self.__arista

    # Valida que no haya aristas repetidas en el grafo
    def __eq__(self, o: object) -> bool:
        if self.getArista()[0] == o.getArista()[0] and self.getArista()[1] == o.getArista()[1]:
          return True
        else:
          return False

    def __str__(self) -> str:
        return f"(Nodo: {self.getArista()[0]}), (Nodo: {self.getArista()[1]}), (Peso: {self.getArista()[2]})"
        
class AristaNoDirigida(Arista):
    def __init__(self, nodo1: Nodo, nodo2: Nodo, peso: int) -> None:
        super().__init__(nodo1, nodo2, peso)

    def dirigido(self) -> bool:
        return False
        
    def getNodo1(self) -> Nodo:
        return self.getArista()[0]

    def getNodo2(self) -> Nodo:
         return self.getArista()[1]

    def getPeso(self) -> int:
        return self.getArista()[2]

    def __str__(self) -> str:
        return f"(Nodo: {self.getArista()[0]}), (Nodo: {self.getArista()[1]}), (Peso: {self.getArista()[2]})"