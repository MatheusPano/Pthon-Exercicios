import json
import os

os.system("cls")

data = {}
data["sp"] = "São Paulo"
data["rj"] = "Rio de Janeiro"
data["mg"] = "Minas Gerais"

#escrever formato json

f = open("data/output.json","w")
json.dump(data,f, sort_keys=True,indent=4)
f.close()



print(data)