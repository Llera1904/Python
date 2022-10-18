from matplotlib import pyplot as plt
import math
from numpy import angle
import re

# Separacion de parte real y parte imaginaria
def separarComplejo(z):
    numeros= re.findall('[0-9]+', z)
    numeroDeMenos= z.count('-')
    numeroDeIs= z.count('i')

    if len(numeros) == 0:
      if numeroDeMenos == 0:
        x= 0
        y= 1

      if numeroDeMenos == 1:
        x= 0
        y= -1
    
    if len(numeros) == 1:
      if numeroDeIs == 0:
        if numeroDeMenos == 0:
          x= float(numeros[0])
          y= 0

        if numeroDeMenos == 1:
          x= -1*float(numeros[0])
          y= 0

      if numeroDeIs == 1:
        if numeroDeMenos == 0:
          x= 0
          y= float(numeros[0])

        if numeroDeMenos == 1:
          x= 0
          y= -1*float(numeros[0])

    if len(numeros) == 2:
      if numeroDeMenos == 0:
        x= float(numeros[0])
        y= float(numeros[1])

      if numeroDeMenos == 1:
        if z.index("-") == 0:
          x= -1*float(numeros[0])
          y= float(numeros[1])
        else:
          x= float(numeros[0])
          y= -1*float(numeros[1])

      if numeroDeMenos == 2:
        x= -1*float(numeros[0])
        y= -1*float(numeros[1])

    print("x: ", x)
    print("y: ", y)

    return x, y

# Funciones de operaciones con complejos
def sumaComplejos(x1, y1, x2, y2):
    x= x1 + x2
    y= y1 + y2

    #print("La suma de z1+z2= (" + str(x) + ")+(" + str(y) + ")i")
    return x, y

def restaComplejos(x1, y1, x2, y2):
    x= x1 - x2
    y= y1 - y2

    #print("La resta de z1-z2= (" + str(x) + ")+(" + str(y) + ")i")
    return x, y

def multiComplejos(x1, y1, x2, y2):
    x= (x1*x2) - (y1*y2)
    y= (x1*y2) + (x2*y1)

    #print("La multiplicacion de z1*z2= (" + str(x) + ")+(" + str(y) + ")i")
    return x, y

def divComplejos(x1, y1, x2, y2):
    numerador= multiComplejos(x1, y1, x2, (y2*-1))
    denominador= multiComplejos(x2, y2, x2, (y2*-1))

    x= round(numerador[0]/denominador[0], 2)
    y= round(numerador[1]/denominador[0], 2)

    #print("La divicion de z1/z2= (" + str(numerador[0]) + "/" + str(denominador[0]) + ")+(" +  str(numerador[1]) + "/" + str(denominador[0]) + ")i")
    #print("La divicion de z1/z2= (" + str(x) + ")+(" + str(y) + ")i")
    return x, y

def potenciaComplejos(x, y, n):
    xCuadrada= pow(x, 2)
    yCuadrada= pow(y, 2)
    modulo= round(pow(xCuadrada+yCuadrada, 1/2), 2)
    #print(modulo)

    argumento= round(math.atan(y/x), 2) # El resultado lo da en radianes
    #argumentoGrados= round((math.atan(y/x))*(180/math.pi), 2) # En grados
    #print(argumento)
    #print(argumentoGrados)

    x= round(pow(modulo, n)*(math.cos(n*argumento)), 2)
    y= round(pow(modulo, n)*(math.sin(n*argumento)), 2)

    return x, y

def raicesComplejos(x, y, n):
    xCuadrada= pow(x, 2)
    yCuadrada= pow(y, 2)
    modulo= round(pow(xCuadrada+yCuadrada, 1/2), 2)
    raizModulo= pow(modulo, 1/n)
    #print(modulo)

    argumento= round(math.atan(y/x), 2) # El resultado lo da en radianes
    #argumentoGrados= round((math.atan(y/x))*(180/math.pi), 2) # En grados
    #print(argumento)
    #print(argumentoGrados)

    parteReal= []
    parteImaginaria= []

    for k in range(n): 
       parteReal.append(round((raizModulo)*(math.cos((argumento+(2*math.pi*k))/(n))), 2))
       parteImaginaria.append(round((raizModulo)*(math.sin((argumento+(2*math.pi*k))/(n))), 2))

    #print(parteReal)
    #print(parteImaginaria)

    return parteReal, parteImaginaria
    
def exponencialComplejos(x, y):
    parteReal= round((pow(math.e, x))*(math.cos(y)), 2)
    parteImaginaria= round((pow(math.e, x))*(math.sin(y)), 2)

    return parteReal, parteImaginaria

def senComplejos(x, y):
    x1, y1= exponencialComplejos((y*-1), x)
    x2, y2= exponencialComplejos(y, (x*-1))
    x3, y3= restaComplejos(x1, y1, x2, y2)
    parteReal, parteImaginaria= divComplejos(x3, y3, 0, 2)

    return parteReal, parteImaginaria

def cosComplejos(x, y):
    x1, y1= exponencialComplejos((y*-1), x)
    x2, y2= exponencialComplejos(y, (x*-1))
    x3, y3= sumaComplejos(x1, y1, x2, y2)
    parteReal, parteImaginaria= divComplejos(x3, y3, 2, 0)

    return parteReal, parteImaginaria

def tanComplejos(x, y):
    x1, y1= senComplejos(x, y)
    x2, y2= cosComplejos(x, y)
    parteReal, parteImaginaria= divComplejos(x1, y1, x2, y2)

    return parteReal, parteImaginaria
    
# Pedimos los numeros complejos, ademas de n y m 
z1= input("Ingresa el primer numero complejo en la forma x+iy: ")
z2= input("Ingresa el segundo numero complejo en la forma x+iy: ")

print("z1= ", z1)
print("z2= ", z2)
x1, y1= separarComplejo(z1)
x2, y2= separarComplejo(z2)

#print("x1= ", x1)
#print("y1= ", y1)
#print("x2= ", x2)
#print("y2= ", y2)

print("\n")

n= input("Ingresa un 'n' entero: ")
m= input("Ingresa un 'm' entero: ")
print("n= ", n)
print("m= ", m)

print("\n")

# Operaciones y puntos a graficar
parteRealP0, parteImaginariaP0= sumaComplejos(x1, y1, x2, y2)
print("La suma de z1+z2= (" + str(parteRealP0) + ")+(" + str(parteImaginariaP0) + ")i")

parteRealP1, parteImaginariaP1= restaComplejos(x1, y1, x2, y2)
print("La resta de z1-z2= (" + str(parteRealP1) + ")+(" + str(parteImaginariaP1) + ")i")

parteRealP2, parteImaginariaP2= multiComplejos(x1, y1, x2, y2)
print("La multiplicacion de z1*z2= (" + str(parteRealP2) + ")+(" + str(parteImaginariaP2) + ")i")

parteRealP3, parteImaginariaP3= divComplejos(x1, y1, x2, y2)
print("La division de z1/z2= (" + str(parteRealP3) + ")+(" + str(parteImaginariaP3) + ")i")

parteRealP4, parteImaginariaP4= potenciaComplejos(x1, y1, int(n))
print("La potencia de z1^" + str(n) + "= (" + str(parteRealP4) + ")+(" + str(parteImaginariaP4) + ")i")

parteRealRaices, parteImaginariaRaices= raicesComplejos(x2, y2, int(m))
print("Las raices de z2:")
for i in range(int(m)):
   print("z" + str(i) + "= (" + str(parteRealRaices[i]) + ")+(" + str(parteImaginariaRaices[i]) + ")i")
  
parteRealP5, parteImaginariaP5= exponencialComplejos(x1, y1)
print("La exponencial de z1= (" + str(parteRealP5) + ")+(" + str(parteImaginariaP5) + ")i")

parteRealP6, parteImaginariaP6= senComplejos(x1, y1)
print("El seno de z1= (" + str(parteRealP6) + ")+(" + str(parteImaginariaP6) + ")i")

parteRealP7, parteImaginariaP7= cosComplejos(x2, y2)
print("El coseno de z2= (" + str(parteRealP7) + ")+(" + str(parteImaginariaP7) + ")i")

parteRealP8, parteImaginariaP8= tanComplejos(parteRealP0, parteImaginariaP0)
print("La tangente de z1+z2= (" + str(parteRealP8) + ")+(" + str(parteImaginariaP8) + ")i")

# Grafica
fig, ax= plt.subplots()

plt.plot(parteRealP0, parteImaginariaP0, marker="o", color="red")
plt.quiver(0, 0 ,parteRealP0, parteImaginariaP0, angles= 'xy', scale_units= 'xy', scale= 1)
plt.plot(parteRealP1, parteImaginariaP1, marker="o", color="blue")
plt.quiver(0, 0 ,parteRealP1, parteImaginariaP1, angles= 'xy', scale_units= 'xy', scale= 1)
plt.plot(parteRealP2, parteImaginariaP2, marker="o", color="green")
plt.quiver(0, 0 ,parteRealP2, parteImaginariaP2, angles= 'xy', scale_units= 'xy', scale= 1)
plt.plot(parteRealP3, parteImaginariaP3, marker="o", color="yellow")
plt.quiver(0, 0 ,parteRealP3, parteImaginariaP3, angles= 'xy', scale_units= 'xy', scale= 1)
plt.plot(parteRealP4, parteImaginariaP4, marker="o", color="gray")
plt.quiver(0, 0 ,parteRealP4, parteImaginariaP4, angles= 'xy', scale_units= 'xy', scale= 1)
plt.plot(parteRealP5, parteImaginariaP5, marker="o", color="black")
plt.quiver(0, 0 ,parteRealP5, parteImaginariaP5, angles= 'xy', scale_units= 'xy', scale= 1)
plt.plot(parteRealP6, parteImaginariaP6, marker="o", color="orange")
plt.quiver(0, 0 ,parteRealP6, parteImaginariaP6, angles= 'xy', scale_units= 'xy', scale= 1)
plt.plot(parteRealP7, parteImaginariaP7, marker="o", color="pink")
plt.quiver(0, 0 ,parteRealP7, parteImaginariaP7, angles= 'xy', scale_units= 'xy', scale= 1)
plt.plot(parteRealP4, parteImaginariaP4, marker="o", color="purple")
plt.quiver(0, 0 ,parteRealP8, parteImaginariaP8, angles= 'xy', scale_units= 'xy', scale= 1)

for i in range(int(m)):
   plt.plot(parteRealRaices[i], parteImaginariaRaices[i], marker="o", color="salmon")
   plt.quiver(0, 0 ,parteRealRaices[i], parteImaginariaRaices[i], angles= 'xy', scale_units= 'xy', scale= 1)   

plt.title("Grafica")
#ax.axis([-10, 10, -5, 5])
plt.show()
