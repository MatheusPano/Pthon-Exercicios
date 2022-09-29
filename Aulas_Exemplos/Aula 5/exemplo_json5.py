import json
import string
import requests
import os

os.system("cls")

navegador = {
    "User-Agent" : "Chrome"
}

url = 'https://parallelum.com.br/fipe/api/v1/carros/marcas/'
codigo = input("Qual o codigo: ")

newUrl = url + codigo + "/modelos"
print(newUrl)

data = requests.get(url=newUrl, headers=navegador)

# print(data.json())

for carro in data.json()["modelos"]:
    print(carro["nome"])