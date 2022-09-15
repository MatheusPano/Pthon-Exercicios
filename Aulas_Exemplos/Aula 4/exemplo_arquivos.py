import os
os.system("cls")

# file_object = open("filename","mode")

# |Value|      |Description|
# ---------------------------
#   'r'         Read Mode
# ---------------------------
#   'w'         Write Mode
# ---------------------------
#   'a'         Append Mode
# ---------------------------
#   'b'         Binary Mode
# ---------------------------
#   '+'         Read/Write Mode
# ---------------------------

f = open("teste.txt", "r")
todas = f.read()
print(todas)
f.close()
