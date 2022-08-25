from mailbox import NotEmptyError
import os
os.system("cls")

def html(nome, endereco, telefone, email, escolaridade, experiencia):
    curriculo = f'''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Nome: {nome}</h1>
    <p>Edereco: {endereco}</p>
    <p>Telefone: {telefone}</p>
    <p>Email: {email}</p>
    <p>Escolaridade: {escolaridade}</p>
    <p>Experiencia: {experiencia}</p>
    
</body>
</html>   
 '''
    arquivo = open('curriculo.html','w',encoding='utf-8')
    arquivo.write(curriculo)
    arquivo.close

nome = input("Nome: ")
endereco = input("endereco: ")
telefone = input("telefone: ")
email = input("email: ")
escolaridade = input("escolaridade: ")
experiencia= input("experiencia: ")

html(nome,endereco,telefone,email,escolaridade,experiencia)