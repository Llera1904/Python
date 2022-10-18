from matplotlib import pyplot as plt
from sympy import *
import sympy as smp
import cmath
import math
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

  return x, y

def centroRadio(circunferencia):
  # Quitamos espacios
  circunferencia= circunferencia.replace(" ", "")   

  # Buscamos los datos que queremos segun la forma en que se metio la ecuacion
  numeros= re.findall(r'-?\d+\.?\d*', circunferencia)

  if len(numeros) == 5:
    h= -1*float(numeros[0])
    k= -1*float(numeros[2])
    r= pow(float(numeros[4]), 1/2)

    return h, k, r
        
  if len(numeros) != 5:
    A= float(numeros[0])
    B= float(numeros[3])
    C= float(numeros[4])
    D= float(numeros[5])

    h= B/-2*A
    k= C/-2*A
    r= pow((pow(B, 2)+pow(C, 2)-(4*D))/4, 1/2)

    return h, k, r

def cuatroPuntosCircunferencia(h, k, r):
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

def calcularDistanciaPuntos(h, k, x, y):
  distancia= pow(pow(x-h, 2)+pow(y-k, 2), 1/2)

  return distancia

print("Programa para calcular una integral con el Teorema de Cauchy\n")

print("Ingresa la funcion de la circunferencia en alguna de las siguientes formas: ")
print("(x-h)^2 + (y-k)^2= r^2")
print("A(x^2 + y^2) + Bx + Cy + D= 0")
circunferencia= input() 
h, k , r= centroRadio(circunferencia)
parteReal, parteImaginaria= cuatroPuntosCircunferencia(h, k, r) 
print("\n")

z0= input("Ingresa z0 en la forma x+iy: ")
x, y= separarComplejo(z0)
print(x, y)
print("\n")

print("Ingresa f(z) en alguna de las siguientes formas:")
print("x+iy\nz^m\ne^z\nsen(z)\ncosh(z)")
funcionZ= input()
print("\n")

n= int(input("ingresa n:"))

# Empieza algoritmo
distancia= calcularDistanciaPuntos(h, k, x, y)
if distancia == r:
  print("Punto sobre r, la integral se indetermina") 

if distancia > r:
  print("Punto fuera de r, integral= 0")

if distancia < r:
  complejo1= complex(0, 2*cmath.pi)
  complejo2= complex(x, y)

  if funcionZ == "x+iy":
    cte= input("ingresa un numero en la forma x+iy: ")
    xReal, yImaginaria= separarComplejo(cte)
    complejoAux= complex(xReal, yImaginaria)
    integral= complejo1*complejoAux
    integral2= 0

  if funcionZ == "z^m":
    m= int(input("ingresa m: "))
    potencia= complejo2**m
    integral= complejo1*potencia

    variable= symbols('x')
    fx= pow(x, m)
    derivada= diff(fx, variable, n-1).subs(variable, complejo2)
    derivada =complex(derivada)
    integral2= complejo1*derivada/math.factorial(n-1)

  if funcionZ == "e^z":
    integral= complejo1*cmath.exp(complejo2)
    integral2= complejo1*cmath.exp(complejo2)/math.factorial(n-1)

  if funcionZ == "sen(z)":
    integral= complejo1*cmath.sin(complejo2)

    variable= symbols('x')
    fx= smp.sin(variable)
    derivada= diff(fx, variable, n-1).subs(variable, complejo2)
    derivada =complex(derivada)
    integral2= complejo1*derivada/math.factorial(n-1)

  if funcionZ == "cosh(z)":
    integral= complejo1*cmath.cosh(complejo2)

    variable= symbols('x')
    fx= smp.cosh(variable)
    derivada= diff(fx, variable, n-1).subs(variable, complejo2)
    derivada =complex(derivada)
    integral2= complejo1*derivada/math.factorial(n-1)
    
  print("integral de f(z)/z-z0= "+str(integral.real)+"+("+str(integral.imag)+")i")
  print("integral de f(z)/(z-z0)^n= "+str(integral2.real)+"+("+str(integral2.imag)+")i")
  
# Graficar
figure, axes= plt.subplots()
circunferencia= plt.Circle((h, k ), r, color='salmon')
plt.plot(parteReal[0], parteImaginaria[0], marker="o", color="black")
plt.plot(parteReal[1], parteImaginaria[1], marker="o", color="black")
plt.plot(parteReal[2], parteImaginaria[2], marker="o", color="black")
plt.plot(parteReal[3], parteImaginaria[3], marker="o", color="black")

# graficamos z0
plt.plot(x, y, marker="x", color="red")

axes.set_aspect(1)
axes.add_artist(circunferencia)
plt.title('circunferencia')

plt.show()