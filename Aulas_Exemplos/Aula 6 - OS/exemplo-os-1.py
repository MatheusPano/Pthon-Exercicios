import os

os.system("cls")

print(os.name)
print(os.getcwd())


#tratamento de exceções
try:
    f = open('xywz.txt','r')
    txt = f.read()
    f.close()
except OSError as e:
    print("Erro ao abrir o arquivo")

