from matplotlib import pyplot as plt
import math
import time

# Cantidad de unos en la cadena 
def amountOne(bin):
    numOne = 0
    for i in range(len(bin)):
        if numberPrimeBin[i] == "1":
            numOne += 1
    return numOne

# Decimal a binario 
def decimalBin(decimal):
    if decimal <= 0:
        return "0"

    binary = ""
    while decimal > 0:
        residuo = int(decimal % 2)
        binary = str(residuo) + binary

        decimal = int(decimal / 2)
    return binary

# Factorial recursivo 
def factorial(x):
    if x == 1:
        return 1

    return x * factorial(x-1)

numFact = factorial(14)
print(numFact)

amountPrimes = int(input("Cantidad de numeros primos: "))
primes = 1
i = 2

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

with open("primos.txt", "w") as txt:
                txt.write('{') 

while  primes <= amountPrimes:
    # fact = factorial(i - 1)
    fact = math.factorial(i - 1)
    # Teorema John Wilson (p-1)! mod p = p-1, p >= 2
    if fact % i == i - 1:
        numberPrime = i
        numberPrimeBin = decimalBin(numberPrime)
        primes += 1
        numOne = amountOne(numberPrimeBin)
        # print(str(numberPrime) + ": " + numberPrimeBin)
        # print(numOne)
        # Graficamos
        plt.plot(i, numOne, markersize=2, marker="o", color="yellow")
        with open("primos.txt", "a") as txt:
                txt.write(str(numberPrime) + ": " + numberPrimeBin + ', ') 
    i += 1

with open("primos.txt", "a") as txt:
                txt.write('...}')

plt.xlim(0, i)
plt.ylim(0, 15)
plt.grid()
plt.show()