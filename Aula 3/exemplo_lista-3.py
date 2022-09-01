import os

os.system("cls")
letras = ["A","B","C","D"]
numeros = [1,2,3]


prod_cart = [(let,num) for let in letras for num in numeros]

for item in prod_cart:
    print(item)