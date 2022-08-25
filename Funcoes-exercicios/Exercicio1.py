import os
os.system("cls")


numeros = []
numPares = 0
numImpares = 0
maior = 0
menor = 99999
media = 0

while True:
    os.system("cls")
    num = int(input("Numero: "))
    numeros.append(num)
    resto = num % 2
    if (resto == 0):
        numPares += 1
    else:
        numImpares += 1

    if (num > maior):
        maior = num
    if (num < menor):
        menor = num

    


    op = input("Deseja continuar? ")
    if(op in "n"):
        os.system("cls")
        break


media = sum(numeros)/len(numeros)
print("Numeros Adicionados: ",numeros)
print("Numeros Pares: ",numPares)
print("Numeros Impares: ",numImpares)
print("Maior Numero: ",maior)
print("Menor Numero: ",menor)
print("Media dos Valores: ", round(media,2))

