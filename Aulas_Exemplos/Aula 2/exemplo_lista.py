import os

os.system("cls")


lista1=[1,2,3]
lista2=[4,5,6]
lista3=[]

lista3.extend(lista1)
lista3.extend(lista2)

for item in lista3:
    print(item)