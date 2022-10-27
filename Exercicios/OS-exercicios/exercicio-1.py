import os

os.system("cls")
dir = os.path.join(os.sep, 'C:\\temp')

contagem = 0
os.chdir(dir)
for i in os.listdir(dir):
    contagem += 1

print(contagem, " Arquivo (s) neste diretório")