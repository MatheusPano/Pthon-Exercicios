import os
os.system("cls")

# set - funcao desordenada mutavel
# frozenset - funcao desordenada nao mutavel

s1 = set("banana")
s2 = set("pera")

s3 = s1 | s2 #Uniao
s4 = s1 & s2 #Interseccao
s5 = s1 - s2 #Diferenca

print("Uniao = %s" %s3)
print("Interseccao = %s" %s4)
print("Diferenca = %s" %s5)
