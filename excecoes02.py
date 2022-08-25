import os
os.system("cls")

vet = "12x45"

for i in range(0,6):
    try:
        print("Quadrado: %d" %(int(vet[i])**2))
    except ValueError:
        print("Valor invalido a posicao: %d" %i)
    except IndexError:
        print("Indice %d maior que o tamanho do vetor" %i)