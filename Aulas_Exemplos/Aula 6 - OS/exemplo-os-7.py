import os

dir = os.path.join(os.sep,'C:\\','Users','2840482011042','Desktop','Python-codes')

for root,dirs,files in os.walk(dir):
    for name in files:
        print(os.path.join(root,name))
    for name in dirs:
        print(os.path.join(root,name))