class Nodo:
    def __init__(self, dato) -> None:
        self.__dato= dato
    
    @property
    def dato(self):
        return self.__dato
    
    def __str__(self):
        return str(self.__dato)

    # Valida que no haya nodos repetidos en el grafo
    def __eq__(self, o: object) -> bool:
        if self.__dato == o.dato:
          return True
        else:
          return False
