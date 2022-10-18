# Para usar: pip install graphviz y descargar en https://graphviz.org/download/
import graphviz as gv

def draw(alfabeto, estados, inicio, transiciones, final):
    print("Inicio: ", inicio)

    g = gv.Digraph(format='svg')
    g.graph_attr['rankdir'] = 'LR' # Pinta el grafico de izquierda a derecha 
    g.node('ini', shape="point")

    for estado in estados:
        if estado in final:
            g.node(estado, shape="doublecircle")
        else:
            g.node(estado)

        if estado in inicio:
            g.edge('ini', estado)

    for transicion in transiciones:
        if transicion[2] not in alfabeto:
            return 0
        
        g.edge(transicion[0], transicion[1], label=transicion[2])

    return g
        
    # g.render(view=True)  

# estados = ["q0", "q1", "q2", "q3"]
# transiciones = [("q0", "q1", "1"), ("q1", "q0", "1"), ("q0", "q2", "0"), ("q2", "q0", "0"),
# ("q1", "q3", "0"), ("q3", "q1", "0"), ("q2", "q3", "1"), ("q3", "q2", "1")]
# inicial = "q0"
# alfabeto = ["0", "1"]
# final = "q0"

estados = ["Ready", "Sending"]
transiciones = [("Ready", "Sending", "dataIn"), ("Sending", "Sending", "timeOut"), ("Sending", "Ready", "ack")]
inicial = "Ready"
alfabeto = ["dataIn", "timeOut", "ack"]
final = "Ready"

g = draw(alfabeto, estados, inicial, transiciones, final)
g.view()

        


        
