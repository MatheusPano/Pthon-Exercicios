import os
os.system("cls")

i = 0
y = 999999

r1 = int(input("Qual o valor da primeira resistencia? "))
if(r1 > i):
    i = r1
if(r1 < y):
    y = r1

r2 = int(input("Qual o valor da segunda resistencia? "))
if(r2 > i):
    i = r2
if(r2 < y):
    y = r2

r3 = int(input("Qual o valor da terceira resistencia? "))
if(r3 > i):
    i = r3
if(r3 < y):
    y = r3

r4 = int(input("Qual o valor da quarta resistencia? "))
if(r4 > i):
    i = r4
if(r4 < y):
    y = r4



print("Resistencias fornecidas: ",r1," ",r2," ", r3, " ", r4)

print("Maior resistencia: ",i)
print("Menor resistencia: ",y)