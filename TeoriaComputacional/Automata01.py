def Automata01(cadenaInput):
    cadenaAceptada = False
    estadoActual = []
    estadoAnterior = []

    with open("camino.txt", "a") as data: # Abre el txt una vez

        estadoActual.append(0) # Estado inicial q0
        for caracter in cadenaInput:

            estadoAnterior = estadoActual
            estadoActual = []

            for estado in estadoAnterior:
                if estado == 0:
                    if caracter == '0':
                        estadoActual.append(0)
                        estadoActual.append(1)
                    elif caracter == '1':
                        estadoActual.append(0)

                elif estado == 1:
                    if caracter == '0':
                        cadenaAceptada = False
                    elif caracter == '1':
                        estadoActual.append(2)
                        cadenaAceptada = True

                elif estado == 2:
                    if caracter == '0':
                        cadenaAceptada = False
                    elif caracter == '1':
                        cadenaAceptada = False

            # print(estadoActual)
            data.write(str(estadoActual) + "\n") # Escribe el camino en un txt
     
    # print(cadenaAceptada)
    if cadenaAceptada == True:
        print("Cadena aceptada")
    else:
        print("Cadena no aceptada")

with open("camino.txt", "w") as data:
    data.write("") 

cadenaInput = "00101"
Automata01(cadenaInput) 
