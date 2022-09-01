import os
import collections

os.system("cls")

produtos = []
Produto = collections.namedtuple("Produto", "Nome Preco")
i = 0
barato = 0
medios = []
mediaCaros = 0

while i <= 2:
    os.system("cls")
    print("Produto ", i+1)
    nome = input("Nome do produto: ")
    preco = float(input("Preco do produto: "))
    if (preco < 50):
        barato += 1

    if (50 < preco < 100):
        medios.append(Produto(nome, preco))

    if (preco > 100):
        mediaCaros = mediaCaros + preco

    produtos.append(Produto(nome, preco))

    i += 1

for p in produtos:
    print("Nome: %s" % p.Nome)
    print("Preço: %f" % p.Preco)
    print("-------------")

mediaCaros = mediaCaros/len(produtos)

print("\n\n")
print("QTD. Produtos abaixo de R$ 50,00: ", barato)

print("Produtos com precos medios: ", medios)

print("Media dos caros: ", mediaCaros)

