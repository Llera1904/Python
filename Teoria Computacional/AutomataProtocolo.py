import random
import time

def paridadCadena(cadena):
    cadenaAceptada = False
    state = 0

    for caracter in cadena:
        if state == 0:
            if caracter == '0':
                state = 2
            elif caracter == '1':
                state = 1

        elif state == 1:
            if caracter == '0':
                state = 3
            elif caracter == '1':
                state = 0

        elif state == 2:
            if caracter == '0':
                state = 0
            elif caracter == '1':
                state = 3

        elif state == 3:
            if caracter == '0':
                state = 1
            elif caracter == '1':
                state = 2

    if state == 0:
        cadenaAceptada = True

    return cadenaAceptada

def cadenaBinaria():
    cadena = ""
    # for i in range(0, 8):
    entero = random.randint(0, 2**64)
    cadena = "{0:064b}".format(entero)
    
    return cadena 

def creaData(tamaño):  

    cadena = ""
    for i in range(tamaño):
        cadena += cadenaBinaria() + "\n"

    return cadena

# def cadenaBinaria(tamaño):
#     cadena = ""

#     for i in range(0, tamaño):
#         numero = random.randint(0, 1)
#         cadena += str(numero)

#     return cadena

# def creaData(tamaño):
#     with open("data.txt", "w") as data:
#             data.write("")  

#     for i in range(tamaño):
#         with open("data.txt", "a") as data:
#             data.write(cadenaBinaria(64) + "\n")

# Programa 

with open("cadenasPares.txt", "w") as data:
    data.write("") 

with open("cadenasImpares.txt", "w") as data:
     data.write("") 

i = 0
amountPares = 0
ampuntImpares = 0
state = random.randint(0, 1) # Protocolo encendido o apagado 
# print("Antes: " + str(state) + "\n")

while state != 0:
    # print("Dentro: " + str(state) + "\n")
    i += 1

    # creaData(1000) # Hacemos la peticion
    with open("data.txt", "w") as data:
        data.write(creaData(1000))

    with open("cadenasPares.txt", "a") as data:
        data.write("\n\nPeticion: " + str(i) + "\n")

    with open("cadenasImpares.txt", "a") as data:
        data.write("\n\nPeticion: " + str(i) + "\n")

    time.sleep(0.003) # Esperamos 3 milisegundos 

    # Leemos las cadenas y las separamos
    with open('data.txt', encoding="utf8") as dataIn:
        for cadena in dataIn:
            par = paridadCadena(cadena)

            if par == True:
                amountPares += 1
                with open("cadenasPares.txt", "a") as data:
                    data.write(cadena)
            else:
                ampuntImpares += 1
                with open("cadenasImpares.txt", "a") as data:
                    data.write(cadena)

    state = random.randint(0, 1) # Protocolo encendido o apagado

print("Fuera: " + str(state) + "\n")
print("Peticiones totales: " + str(i))
print("Cadenas aceptadas: " + str(amountPares))
print("Cadenas no aceptadas: " + str(ampuntImpares))
print("Total cadenas:" + str(amountPares + ampuntImpares))
