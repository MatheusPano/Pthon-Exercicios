import os

os.system("cls")


i = 0

numeros = []
pares = 0
impares = 0
soma = 0
maior = 0
menor = 9999999

while i < 6:
    num = int(input("Digite o numero: "))
    resto = num % 2
    soma += num
    numeros.append(num)
    if(resto==0):
        pares += 1
    else:
        impares += 1
    
    if (num > maior):
        maior = num
    
    if (num < menor):
        menor = num

    
    i+=1

os.system("cls")
print("Numeros inseridos:", numeros)
print("Qtd numeros pares: ",pares)
print("Qtd numeros impares: ",impares)
print("Soma: ", soma)
print("Maior numero: ", maior)
print("Menor numero: ", menor)
print("------------------------")