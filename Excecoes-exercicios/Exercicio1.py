import os
os.system("cls")
listaGeral = []



while True:
    try:
        peso = float(input("Peso: "))
        altura = float(input("Altura: "))
        imc = peso/altura**2
        pessoa = [peso, altura, round(imc,2)]
        listaGeral.append(pessoa)
        
    except ValueError as erro:
        print("Valor invalido")
    
    os.system("cls")
    op = input("Deseja continuar? s/n ")
    if(op in "n"):
        break

print(listaGeral)