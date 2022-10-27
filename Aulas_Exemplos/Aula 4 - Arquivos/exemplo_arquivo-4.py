import os
os.system("cls")

import csv


# Leitura do arquivo
f = open("data/sample.csv","r",encoding="iso-8859-1")
reader = csv.reader(f)
for row in reader:
    print(row)

f.close()