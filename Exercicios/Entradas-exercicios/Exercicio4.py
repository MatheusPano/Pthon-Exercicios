import os
os.system("cls")

year = int(input("Ano: "))


resto = year % 100
seculo = year / 100 


if(resto != 0):
    seculo += 1
    print("Século: ", int(seculo))
else:
    print("Século: ", int(seculo)) 
