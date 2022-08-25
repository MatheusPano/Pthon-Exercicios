# Calculo do imc

peso = float(input("Qual o peso da pessoa: "))
altura = float(input("Qual a altura da pessoa: "))

imc = (peso/(altura*altura))
print("O imc dessa pessoa é de ->", imc)

if imc < 18.5:
    print("Abaixo do peso normal")
elif 18.5 < imc < 24.9:
    print("Peso Normal")
elif 25 < imc < 29.9:
    print("Excesso de peso")
elif 30 < imc < 34.9:
    print("Obesidade de classe I")
elif 35 < imc < 39.9:
    print("Obesidade de Classe II")
elif imc >=40:
    print("Obesidade Classe III")
