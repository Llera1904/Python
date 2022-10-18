from matplotlib import pyplot as plt
from matplotlib import pyplot
import math
from numpy import angle
import re

def separarEntrada(circunferencia):
    aDiferenteCero= True
    # Quitamos espacios
    circunferencia= circunferencia.replace(" ", "")   

    # Buscamos los datos que queremos segun la forma en que metio la ecuacion
    #numeros= re.findall('[0-9]+', circunferencia)
    numeros= re.findall(r'-?\d+\.?\d*', circunferencia)
    #print(numeros)

    if len(numeros) == 5:
      h= -1*float(numeros[0])
      k= -1*float(numeros[2])
      r= pow(float(numeros[4]), 1/2)

      return h, k, r, aDiferenteCero
        
    if len(numeros) != 5:
      A= float(numeros[0])
      B= float(numeros[3])
      C= float(numeros[4])
      D= float(numeros[5])

      if A != 0:
        h= B/-2*A
        k= C/-2*A
        r= pow((pow(B, 2)+pow(C, 2)-(4*D))/4, 1/2)

        return h, k, r, aDiferenteCero

      if A == 0:
        aDiferenteCero= False
        return B, C, D, aDiferenteCero

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

    #print("x: ", x)
    #print("y: ", y)

    return x, y

# Funciones de operaciones con complejos
def sumaComplejos(x1, y1, x2, y2):
    x= x1 + x2
    y= y1 + y2

    return x, y

def restaComplejos(x1, y1, x2, y2):
    x= x1 - x2
    y= y1 - y2

    return x, y

def multiComplejos(x1, y1, x2, y2):
    x= (x1*x2) - (y1*y2)
    y= (x1*y2) + (x2*y1)

    return x, y

def divComplejos(x1, y1, x2, y2):
    numerador= multiComplejos(x1, y1, x2, (y2*-1))
    denominador= multiComplejos(x2, y2, x2, (y2*-1))

    x= numerador[0]/denominador[0]
    y= numerador[1]/denominador[0]

    #x= round(numerador[0]/denominador[0], 2)
    #y= round(numerador[1]/denominador[0], 2)

    return x, y

def sacarCuatroPuntosCircunferencia(h, k, r):
   xpunto1= h
   ypunto1= k+r

   xpunto2= h+r
   ypunto2= k

   xpunto3= h
   ypunto3= k-r

   xpunto4= h-r
   ypunto4= k

   parteReal= xpunto1, xpunto2, xpunto3, xpunto4
   parteImaginaria= ypunto1, ypunto2, ypunto3, ypunto4

   return parteReal, parteImaginaria

def aplicarMobius(x, y, x1, y1, x2, y2, x3, y3, x4, y4):
    
    multi1Real, multi1Imaginaria= multiComplejos(x1, y1, x, y)
    multi2Real, multi2Imaginaria= multiComplejos(x3, y3, x, y)
    numeradorparteReal, numeradorParteImaginaria= sumaComplejos(multi1Real, multi1Imaginaria, x2, y2) 
    denominadorParteReal, denominadorParteImaginaria= sumaComplejos( multi2Real, multi2Imaginaria, x4, y4)
    parteReal, parteImaginaria= divComplejos(numeradorparteReal, numeradorParteImaginaria, denominadorParteReal, denominadorParteImaginaria)
    
    return parteReal, parteImaginaria

def calcularNuevaCircunferencia(parteRealFuncion, parteImaginariaFuncion):
    A1= (2*parteRealFuncion[1])-(2*parteRealFuncion[0])
    A2= (2*parteRealFuncion[2])-(2*parteRealFuncion[0])
    B1= (2*parteImaginariaFuncion[1])-(2*parteImaginariaFuncion[0])
    B2= (2*parteImaginariaFuncion[2])-(2*parteImaginariaFuncion[0])
    C1= (pow(parteRealFuncion[1], 2)+pow(parteImaginariaFuncion[1], 2))-(pow(parteRealFuncion[0], 2)+pow(parteImaginariaFuncion[0], 2))
    C2= (pow(parteRealFuncion[2], 2)+pow(parteImaginariaFuncion[2], 2))-(pow(parteRealFuncion[0], 2)+pow(parteImaginariaFuncion[0], 2))

    h= ((C1*B2)-(C2*B1))/((A1*B2)-(A2*B1))
    k= ((C1*A2)-(C2*A1))/((B1*A2)-(B2*A1))
    r= pow((pow(parteRealFuncion[0], 2)-(2*parteRealFuncion[0]*h)+pow(h, 2)+pow(parteImaginariaFuncion[0], 2)-(2*parteImaginariaFuncion[0]*k)+pow(k, 2)), 1/2)

    #return round(h, 2), round(k, 2), round(r, 2)
    return h, k, r

print("Programa para calcular la funcion Mobius dada una circunferencia")
print("Ingresa la funcion de la circunferencia en alguna de las siguientes formas: ")
print("(x-h)^2 + (y-k)^2= r^2")
print("A(x^2 + y^2) + Bx + Cy + D= 0")
circunferencia= input() 
x, y, z, aDiferenteCero= separarEntrada(circunferencia)

# Pedimos los 4 numeros complejos y los separamos en su parte real y su parte imaginaria
z1= input("Ingresa un complejo en la forma x+iy: ")
z2= input("Ingresa un complejo en la forma x+iy: ")
z3= input("Ingresa un complejo en la forma x+iy: ")
z4= input("Ingresa un complejo en la forma x+iy: ")

print(z1)
print(z2)
print(z3)
print(z4)

x1, y1= separarComplejo(z1)
x2, y2= separarComplejo(z2)
x3, y3= separarComplejo(z3)
x4, y4= separarComplejo(z4)

if aDiferenteCero == True:
  h, k, r= x, y, z

  if (z1 == z2) and (z2 == z3) and (z3 == z4):
    print("Error. Los 4 numeros complejos no pueden ser iguales")

  if (x1 == 0 and x2 == 0) and (y1== 0 and y2 == 0):
    print("z1 y z2 no pueden ser iguales a 0")

  if (x3 == 0 and x4 == 0) and (y3== 0 and y4 == 0):
    print("z3 y z4 no pueden ser iguales a 0")

  if ((x1 != 0 or x2 != 0) or (y1!= 0 or y2 != 0)) and ((x3 != 0 or x4 != 0) or (y3!= 0 or y4 != 0)) and not((z1 == z2) and (z2 == z3) and (z3 == z4)):
    # Sacamos los tres puntos de las circunferencia 
    parteReal, parteImaginaria= sacarCuatroPuntosCircunferencia(h, k, r)
    print("Los numeros complejos a trasformar son: ")

    for i in range(3):
       print("z" + str(i) + "= (" + str(parteReal[i]) + ")+(" + str(parteImaginaria[i]) + ")i")

    print("z0(negro), z1(azul), z2(rojo)")
    h, k, r= calcularNuevaCircunferencia(parteReal, parteImaginaria)
    print("C(" + str(h) + ", " + str(k) + ") " + "r= " + str(r))

    # Aplicamos la funcion   
    parteRealFuncion= []
    parteImaginariaFuncion= []

    for i in range(3):
       x, y= aplicarMobius(parteReal[i], parteImaginaria[i], x1, y1, x2, y2, x3, y3, x4, y4)
       parteRealFuncion.insert(i, x)
       parteImaginariaFuncion.insert(i, y)

    print("Los numeros complejos aplicando la funcion son: ")
    for i in range(3):
       print("z" + str(i) + "= (" + str(parteRealFuncion[i]) + ")+(" + str(parteImaginariaFuncion[i]) + ")i")

    # Calculamos la nueva circunferencia
    print("z0(negro), z1(azul), z2(rojo)")
    hTransformado, kTrasnformado, rTransformado= calcularNuevaCircunferencia(parteRealFuncion, parteImaginariaFuncion)
    print("C(" + str(hTransformado) + ", " + str(kTrasnformado) + ") " + "r= " + str(rTransformado))

    # Graficar circinferenciaS
    figure, axes= plt.subplots()
    circunferencia= plt.Circle((h, k ), r, color='orange', fill= False)
    plt.plot(parteReal[0], parteImaginaria[0], marker="x", color="black")
    plt.plot(parteReal[1], parteImaginaria[1], marker="x", color="blue")
    plt.plot(parteReal[2], parteImaginaria[2], marker="x", color="red")
    plt.plot(parteReal[3], parteImaginaria[3], marker="o", color="orange")

    axes.set_aspect(1)
    axes.add_artist(circunferencia)
    plt.title('circunferencia1')

    figure, axes= plt.subplots()
    circunferencia2= plt.Circle((hTransformado, kTrasnformado), rTransformado, color='salmon', fill= False)
    plt.plot(parteRealFuncion[0], parteImaginariaFuncion[0], marker="x", color="black")
    plt.plot(parteRealFuncion[1], parteImaginariaFuncion[1], marker="x", color="blue")
    plt.plot(parteRealFuncion[2], parteImaginariaFuncion[2], marker="x", color="red")

    parteReal, parteImaginaria= sacarCuatroPuntosCircunferencia(hTransformado, kTrasnformado, rTransformado)
    plt.plot(parteReal[0], parteImaginaria[0], marker="o", color="salmon")
    plt.plot(parteReal[1], parteImaginaria[1], marker="o", color="salmon")
    plt.plot(parteReal[2], parteImaginaria[2], marker="o", color="salmon")
    plt.plot(parteReal[3], parteImaginaria[3], marker="o", color="salmon")

    axes.set_aspect(1)
    axes.add_artist(circunferencia2)
    plt.title('circunferencia2')

    plt.show()
else:
  print("Error. A debe ser distinto de 0")
  print("Si A= 0, solo se grafica una recta")
  B, C, D= x, y, z

  # Sacamos 3 puntos de la recta
  parteReal= []
  parteImaginaria= []
  for i in range(3):
     parteReal.insert(i, i) 
     parteImaginaria.insert(i, ((-B*i)-(D))/C)

  x= range(-10, 10)
  recta1= pyplot.plot(x, [(((-B*i)-(D))/C) for i in x])
  plt.title('recta1')

  plt.plot(parteReal[0], parteImaginaria[0], marker="x", color="black")
  plt.plot(parteReal[1], parteImaginaria[1], marker="x", color="blue")
  plt.plot(parteReal[2], parteImaginaria[2], marker="x", color="red")

  # Establecemos el color de los ejes.
  pyplot.axhline(0, color="black")
  pyplot.axvline(0, color="black")

  # Especificamos los limites de los ejes.
  pyplot.xlim(-11, 11)
  pyplot.ylim(-11, 11)

  # Aplicamos la funcion   
  parteRealFuncion= []
  parteImaginariaFuncion= []
  for i in range(3):
     x, y= aplicarMobius(parteReal[i], parteImaginaria[i], x1, y1, x2, y2, x3, y3, x4, y4)
     parteRealFuncion.insert(i, x)
     parteImaginariaFuncion.insert(i, y)

  print("Los numeros complejos aplicando la funcion son: ")
  for i in range(3):
     print("z" + str(i) + "= (" + str(parteRealFuncion[i]) + ")+(" + str(parteImaginariaFuncion[i]) + ")i")

  # Calculamos la nueva circunferencia
  print("z0(negro), z1(azul), z2(rojo)")
  hTransformado, kTrasnformado, rTransformado= calcularNuevaCircunferencia(parteRealFuncion, parteImaginariaFuncion)
  print("C(" + str(hTransformado) + ", " + str(kTrasnformado) + ") " + "r= " + str(rTransformado))

  figure, axes= plt.subplots()
  circunferencia2= plt.Circle((hTransformado, kTrasnformado), rTransformado, color='salmon', fill= False)
  plt.plot(parteRealFuncion[0], parteImaginariaFuncion[0], marker="x", color="black")
  plt.plot(parteRealFuncion[1], parteImaginariaFuncion[1], marker="x", color="blue")
  plt.plot(parteRealFuncion[2], parteImaginariaFuncion[2], marker="x", color="red")

  parteReal, parteImaginaria= sacarCuatroPuntosCircunferencia(hTransformado, kTrasnformado, rTransformado)
  plt.plot(parteReal[0], parteImaginaria[0], marker="o", color="salmon")
  plt.plot(parteReal[1], parteImaginaria[1], marker="o", color="salmon")
  plt.plot(parteReal[2], parteImaginaria[2], marker="o", color="salmon")
  plt.plot(parteReal[3], parteImaginaria[3], marker="o", color="salmon")

  axes.set_aspect(1)
  axes.add_artist(circunferencia2)
  plt.title('circunferencia2')

  # Mostramos el gráfico.
  pyplot.show()

