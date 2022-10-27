import os

dir = os.path.join(os.sep, 'c:\\', 'temp')

if(not os.path.exists(dir)):
    os.makedirs(dir)

os.chdir(dir)
for i in os.listdir(dir):
    os.rmdir(str(i))