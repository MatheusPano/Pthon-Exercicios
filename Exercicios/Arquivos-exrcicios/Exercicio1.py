import os
os.system("cls")


n = range(2)

f = open("teste.txt","r")

for linhas in n:
    f.readlines(linhas)
    print(linhas)



f.close()