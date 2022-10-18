from matplotlib import pyplot as plt
from numpy import double
import sympy as smp
import cmath
import math

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

def calcularResiduo(m, n, a, b, c, grado, complejo):
  variable= smp.symbols('z')
  # Creamos los complejos para la funcion f(z)
  complejo2= complex(0, a)
  complejo3= complex(b, 0)
  complejo4= complex(0, c)

  numerador= variable**n
  denominador= ((variable - complejo2)**m) * (variable - complejo3) * ((variable + complejo4)**4)
  fz= numerador/denominador
  funcion= ((variable - complejo)**grado) * (fz)

  if grado > 1:
    derivada= smp.diff(funcion, variable, grado-1).subs([(variable, complejo)]).evalf()

  if grado == 1:
    derivada= funcion.subs([(variable, complejo)]).evalf()

  residuo= (1/math.factorial(grado-1)) * derivada

  return residuo

print("Programa para calcular una integral con el Teorema del residuo\n")

m= int(input("ingresa m: "))
n= int(input("ingresa n: "))
a= int(input("ingresa a: "))
b= int(input("ingresa b: "))
c= int(input("ingresa c: "))
r= double(input("ingresa r: "))
parteReal, parteImaginaria= cuatroPuntosCircunferencia(0, 0, r) 
print("\n")

distancia1= calcularDistanciaPuntos(0, 0, 0, a)
distancia2= calcularDistanciaPuntos(0, 0, b, 0)
distancia3= calcularDistanciaPuntos(0, 0, 0, -1*c)
# print(distancia1, distancia2, distancia3)

dentroCurvaPunto= [False, False, False]
sobreCurvaPunto= [False, False, False]
puntosDentroCurva= [] 

# Preguntamos si los puntos estan dentro de la curva r y guardamos que puntos lo estan
if distancia1 < r:
  dentroCurvaPunto[0]= True
  puntosDentroCurva.append(complex(0, a))

if distancia2 < r:
  dentroCurvaPunto[1]= True
  puntosDentroCurva.append(complex(b, 0))

if distancia3 < r:
  dentroCurvaPunto[2]= True
  puntosDentroCurva.append(complex(0, -1*c))

# Preguntamos si los puntos estan sobre la curva r
if distancia1 == r:
  sobreCurvaPunto[0]= True

if distancia2 == r:
  sobreCurvaPunto[1]= True

if distancia3 == r:
  sobreCurvaPunto[2]= True

# print(fueraCurvaPunto)
# print(sobreCurvaPunto)

# Validaciones
if True in sobreCurvaPunto: 
  print("Punto sobre r, la integral se indetermina") 
  
if (distancia1 > r) and (distancia2 > r) and (distancia3 > r):
  print("Puntos fuera de r, integral= 0")

if True in dentroCurvaPunto: 
  complejo= complex(0, 2*cmath.pi)
  sumaResiduos= 0
  for i in range(len(puntosDentroCurva)):
     if puntosDentroCurva[i] == complex(0, a):
       grado= m
     
     if puntosDentroCurva[i] == complex(b, 0):
       grado= 1

     if puntosDentroCurva[i] == complex(0, -1*c):
       grado= 4
    
     residuo= calcularResiduo(m, n, a, b, c, grado, puntosDentroCurva[i])
     sumaResiduos= sumaResiduos + residuo
     integral= complejo*complex(sumaResiduos)

  # print(sumaResiduos)
  print("integral de (z^n)/((z-ai)^m(z-b)(z+ci)^4)= "+str(integral.real)+"+("+str(integral.imag)+")i")

# Graficar
figure, axes= plt.subplots()
circunferencia= plt.Circle((0, 0), r, color='salmon')
plt.plot(parteReal[0], parteImaginaria[0], marker="o", color="black")
plt.plot(parteReal[1], parteImaginaria[1], marker="o", color="black")
plt.plot(parteReal[2], parteImaginaria[2], marker="o", color="black")
plt.plot(parteReal[3], parteImaginaria[3], marker="o", color="black")

# graficamos a, b, c
plt.plot(0, a, marker="x", color="red")
plt.plot(b, 0, marker="x", color="black")
plt.plot(0, -1*c, marker="x", color="green")

axes.set_aspect(1)
axes.add_artist(circunferencia)
plt.title('circunferencia')

plt.show()