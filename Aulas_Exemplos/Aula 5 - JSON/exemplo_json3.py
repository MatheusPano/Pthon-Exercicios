import json

data = {}

data["vermelho"] = {"nome": "Vermelho", "rgb": "255,0,0", "hex": "#FFFF00"}
data["verde"] = {"nome": "Verde", "rgb": "0,255,0", "hex": "#00FF00"}
data["azul"] = {"nome": "Azul", "rgb": "0,0,255", "hex": "#0000FF"}

# escrever formato JSON
f = open("data/output.json", "w")
json.dump(data, f, sort_keys=True, indent=4)
f.close()
