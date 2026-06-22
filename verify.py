import hashlib

try:
    with open("hash.txt","r") as hashfile:
        path=hashfile.readline().strip()
        hash_value=hashfile.readline().strip()
except FileNotFoundError:
    print("File not found")
    exit()
path2=input("Enter file you want to check:")
try:
    with open(path2,"rb") as file:
        data=file.read()
        new_value=hashlib.sha256(data).hexdigest()
except FileNotFoundError:
    print("File not found")
    exit()
if new_value==hash_value and path==path2:
    print("File:",path)
    print("file is safe")
elif path!=path2:
    print("Differnt files")
else:
    print("Danger: file modified")