import json
import requests
import os

os.system("cls")

navegador = {
    "User-Agent" : "Chrome"
}

url = 'https://parallelum.com.br/fipe/api/v1/carros/marcas'

data = requests.get(url=url, headers=navegador)
# print(data.json())

for marca in data.json():
    print(marca)

# print(data)