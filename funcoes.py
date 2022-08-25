import os

def limpar_tela():
    os.system("cls")

def ler_numero():
    return int(input("Informe um valor: "))

def soma(n1, n2):
    return n1+n2

def main():
    limpar_tela()
    n1 = ler_numero()
    n2 = ler_numero()
    print("O resultado da sua soma é:", soma(n1,n2))


main()