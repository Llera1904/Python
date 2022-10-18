from matplotlib import pyplot as plt

# Cantidad de unos en la cadena 
def amountOne(bin):
    numOne = 0
    for i in range(len(bin)):
        if bin[i] == "1":
            numOne += 1
    return numOne

def setString(setK):
    alphabet = ['0', '1']
    newSetK = []

    for i in range(len(alphabet)):
        for j in range(len(setK)):
            combination = alphabet[i] + setK[j]
            with open("universo.txt", "a") as txt:
                txt.write(combination + ', ')          
            newSetK.append(combination) 

    return newSetK

def setStringBin(m, amountStrings):
    bin = []
    for i in range(2**m):
        binAux = format(i, "0" + str(m) + "b")
        bin.append(binAux)
        amountStrings += 1
        with open("universo.txt", "a") as txt:
                txt.write(binAux + ', ')

        numOne = amountOne(binAux)
        plt.plot(amountStrings, numOne, markersize=4, marker="o", color="yellow")        

    return bin, amountStrings         


print("Programa que calcula el universo m de ∑= {0, 1}")
m = int(input("Introduce el valor de m: "))

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

with open("universo.txt", "w") as txt:
    txt.write('{e, ')

setK = [""]
amountStrings = 0
for i in range(m):
    # setK = setString(setK) 
    setK, amountStrings = setStringBin(i + 1, amountStrings)
    # print(setK)

with open("universo.txt", "a") as txt:
    txt.write('...}')  
    
plt.xlim(0, amountStrings)
plt.ylim(0, m)
plt.grid()
plt.show()

