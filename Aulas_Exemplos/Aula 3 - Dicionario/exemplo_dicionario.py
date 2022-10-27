import os
os.system("cls")

print("\t\t\t\t\t\t\t\tDICIONARIO")

dic = dict({"nome":"Joao da Silva","idade":22})

for chave,valor in dic.items():
    print("%s = %s" %(chave,valor))