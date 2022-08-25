import os
os.system("cls")

nome_produto = input("Qual o produto? ")

valor_original = float(input("Qual o valor desse produto? "))

valor_novo = 0

if (valor_original < 0):
    print("Erro, valor invalido")
elif (50 <= valor_original < 200):
    desconto = 0.05 * valor_original
    valor_novo = valor_original - desconto
elif (200 <= valor_original < 500):
    desconto = 0.06 * valor_original
    valor_novo = valor_original - desconto
elif (500 <= valor_original < 1000):
    desconto = 0.07 * valor_original
    valor_novo = valor_original - desconto
elif (1000 <= valor_original):
    desconto = 0.08 * valor_original
    valor_novo = valor_original - desconto
else: 
    print("Sem descontos")


print(valor_novo)