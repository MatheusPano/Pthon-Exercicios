import os
os.system("cls")

#módulo para serialização de dados
import pickle as pk

v1 = "Hello World!"
v2 = ["Joao da Silva","Ana Maria"]

# Escrever arquivo binário
f = open("data.dat","wb")
pk.dump(v1,f)
pk.dump(v2,f)
f.close()

# Leitura arquivo binário
f = open("data.dat", "rb")
v1 = pk.load(f)
v2 = pk.load(f)
print(v1)
print(v2)
f.close()