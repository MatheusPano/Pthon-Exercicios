from asyncio.windows_events import NULL
import json
import string
import requests
import os

os.system("cls")

navegador = {
    "User-Agent" : "Chrome"
}

# https://parallelum.com.br/fipe/api/v1/carros/marcas/21/modelos/6885/anos/2017-1

url = 'https://parallelum.com.br/fipe/api/v1/carros/marcas/'
codigo = input("Qual o codigo: ")

newUrl = url + codigo + "/modelos"
codigoModelo = input("qual o codigo do modelo: ")
newUrl = newUrl + "/" + codigoModelo + "/anos/"
ano = input("Qual o ano que deseja ver: ")
newUrl = newUrl + ano
print(newUrl)

data = requests.get(url=newUrl, headers=navegador)
os.system("cls")
print(newUrl)


print(data.json())
