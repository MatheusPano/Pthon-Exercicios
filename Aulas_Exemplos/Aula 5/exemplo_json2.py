import json
import os

os.system("cls")


#ler formato json

f = open("data/output.json","r")
data = json.load(f)
f.close()



print(data)