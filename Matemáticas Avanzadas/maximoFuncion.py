from sqlalchemy import false
from sympy import symbols, solve 
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import sympy as smp

# Funcion para calcular el vector de direccion U
def calcularU(a, b, c, d, x, y):
  variableX= smp.symbols('x')
  variableY= smp.symbols('y')

  funcion= a*(variableX**2 + variableY**2) + b*variableX + c*variableY + d
  derivadaParcialX= smp.diff(funcion, variableX, 1).subs([(variableX, x)]).evalf()
  derivadaParcialY= smp.diff(funcion, variableY, 1).subs([(variableY, y)]).evalf()

  moduloU= pow(derivadaParcialX**2 + derivadaParcialY**2, 1/2)
  uX= derivadaParcialX/moduloU
  uY= derivadaParcialY/moduloU

  return uX, uY

def puntoCritico(a, b, c, d): 
  variableX= smp.symbols('x')
  variableY= smp.symbols('y')

  funcion= a*(variableX**2 + variableY**2) + b*variableX + c*variableY + d
  derivadaParcialX= smp.diff(funcion, variableX, 1)
  derivadaParcialY= smp.diff(funcion, variableY, 1)
  derivadaParcialXY= smp.diff(derivadaParcialX, variableY, 1)

  SegundaDerivadaParcialX= smp.diff(funcion, variableX, 2)
  SegundaderivadaParcialY= smp.diff(funcion, variableY, 2)

  solucionParcialX= solve(derivadaParcialX) 
  solucionParcialY= solve(derivadaParcialY) 
  if len(solucionParcialX) != 0 and len(solucionParcialY) != 0:
    punto= (solucionParcialX[0], solucionParcialY[0])
    noHayMaximo= False

  if len(solucionParcialX) == 0 and len(solucionParcialY) == 0:
    punto= (0, 0)
    noHayMaximo= True

  d= SegundaDerivadaParcialX*SegundaderivadaParcialY - (derivadaParcialXY**2)

  return punto, d, SegundaDerivadaParcialX, noHayMaximo

print("Programa para calcular el maximo de una funcion\n")

n= int(input("ingresa n: "))
a= int(input("ingresa a: "))
b= int(input("ingresa b: "))
c= int(input("ingresa c: "))
d= int(input("ingresa d: "))
print("\n")
print("Ingresa un punto de la forma (x, y): ")
x= int(input("Ingresa x: "))
y= int(input("Ingresa y: "))
print("Punto Original: ("+str(x)+", "+str(y)+")")
print("\n")

# Camino hacia el maximo
variableX= smp.symbols('x')
variableY= smp.symbols('y')
funcion= a*(variableX**2 + variableY**2) + b*variableX + c*variableY + d

puntos= []
puntosEvaluados= []
for i in range(n):
   punto= (x, y)
   puntos.append(punto)
   
   # Evaluamos los puntos para obtener Z
   funcionEvaluada= funcion.subs([(variableX, x)]).evalf()
   funcionEvaluada= funcionEvaluada.subs([(variableY, y)]).evalf()
   z= funcionEvaluada
   puntoEvaludo= (x, y ,z)
   puntosEvaluados.append(puntoEvaludo)

   u= calcularU(a, b, c, d, x, y)
   x= x + u[0]
   y= y + u[1] 
   
print("puntos: ", puntos)
print("\n")
print("Puntos Evaluados: ", puntosEvaluados)

# Calcular punto critico y si es maximo o minimo
punto, d, SegundaDerivadaParcialX, noHayMaximo= puntoCritico(a, b, c, d)
print("\n")
if noHayMaximo == False:
  print("Punto critico en : " + str(punto))

  if d > 0 and SegundaDerivadaParcialX > 0:
    print("Punto:" + str(punto) + " es un minimo relativo\n\n\n")

  if d > 0 and SegundaDerivadaParcialX < 0:
    print("Punto:" + str(punto) + " es un maximo relativo\n\n\n")

  if d < 0:
    print("Punto:" + str(punto) + " es un punto silla\n\n\n")

  if d == 0:
    print("Punto:" + str(punto) + " no es concluyente\n\n\n")

  # Evaluamos los puntos para obtener Z
  funcionEvaluada= funcion.subs([(variableX, punto[0])]).evalf()
  funcionEvaluada= funcionEvaluada.subs([(variableY, punto[1])]).evalf()
  zPuntoCritico= funcionEvaluada

if noHayMaximo == True:
  print("No hay punto critico")

# Graficar
fig= plt.figure()
ax= Axes3D(fig)

x= np.linspace(-20, 20, 20)
y= np.linspace(-20, 20, 20)

X, Y= np.meshgrid(x, y)
ax.plot_surface(X, Y, a*(X**2 + Y**2) + b*X + c*Y + d)
# Graficamos puntos
for i in range(len(puntos)):
   ax.scatter(puntos[i][0], puntos[i][1], 0, color= "red")

for i in range(len(puntos)):
   ax.scatter(puntosEvaluados[i][0], puntosEvaluados[i][1], puntosEvaluados[i][2], color="black")

if noHayMaximo == False:
  ax.scatter(punto[0], punto[1], 0, color= "orange")
  ax.scatter(punto[0], punto[1], zPuntoCritico, color="blue")

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

