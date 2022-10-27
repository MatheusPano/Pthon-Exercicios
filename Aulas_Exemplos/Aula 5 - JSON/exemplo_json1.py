import json
import os

os.system("cls")

data = {}
data["sp"] = "São Paulo"
data["rj"] = "Rio de Janeiro"
data["mg"] = "Minas Gerais"

#escrever formato json

f = open("data/output.json","w", encoding='utf8')
json.dump(data,f, sort_keys=True,indent=4, ensure_ascii=False)
f.close()



print(data)