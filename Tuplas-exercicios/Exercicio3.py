import os
import collections

os.system("cls")


Alunos =[]
Aluno = collections.namedtuple("Aluno", "Nome Nota1 Nota2 Média Situacao")
i = 0
aprovados = 0
reprovados = 0
mediaClasse = 0


while i <= 5:
    os.system("cls")
    print("Aluno ", i+1)
    nome = input("Nome: ")
    num1 = float(input("Primeira nota: "))
    num2 = float(input("Segunda nota: "))
    media = (num1 + num2)/2
    situacao = ""
    if (media >= 6):
        situacao = "Aprovado"
        aprovados+=1
    else:
        situacao = "Reprovado"
        reprovados+=1

    mediaClasse = mediaClasse + media
    Alunos.append(Aluno(nome, num1,num2,media,situacao))
    i+=1

os.system("cls")
for p in Alunos:
    print("Aluno: %s" %p.Nome)
    print("Nota 1:%f" %p.Nota1)
    print("Nota 2: %f" %p.Nota2)
    print("Média: %f" %p.Média)
    print("Situação: %s" %p.Situacao)
    print("-------------------")

mediaClasse = mediaClasse/len(Alunos)
print("Média da Classe: ", mediaClasse)
print("Qtd Aprovados: ", aprovados)
print("Qtd Reprovados: ",reprovados)