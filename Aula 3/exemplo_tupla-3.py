import collections
import os
import collections

os.system("cls")

Pessoa = collections.namedtuple("Pessoa","id nome idade email")

pessoas=[]

pessoas.append(Pessoa(1,"Joao da Silva", 22, "joao@joao.com"))
pessoas.append(Pessoa(2,"Ana Maria", 19, "maria@na.com"))
pessoas.append(Pessoa(3,"Matheus", 20,"panomatheus@mail.com"))


for p in pessoas:
    print("Id: %d"  %p.id)
    print("Nome: %s" %p.nome)
    print("Idade: %d" %p.idade)
    print("Email: %s" %p.email)
    print("-------------------")
