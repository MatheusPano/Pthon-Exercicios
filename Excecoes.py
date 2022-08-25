import os
os.system("cls")

s = "aeiou"

try:
    print(s[5])
except IndexError as erro:
    print("A posicao nao foi encontrada")
    print(erro)
