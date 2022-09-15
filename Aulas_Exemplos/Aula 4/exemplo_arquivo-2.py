import os
os.system("cls")

# Escrita
f = open("data.txt", "w")
f.write("Primeira Linha de texto\n")
f.write("Segunda linha de texto\n")
f.close()

# Escrita no final
f = open("data.txt", "a")
f.write("Terceira linha de texto\n")
f.close()

# Leitura
f = open("data.txt", "r")
print(f.read())
f.close()