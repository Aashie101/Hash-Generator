import hashlib

print("=== SHA256 File Hash Generator ===")

path= "important.txt"
try:
    with open(path,"rb") as file:
        data=file.read()
except FileNotFoundError:
    print("File not found")
    exit()
#encode(): converts a string to bytes
#hexdigest() converts the hash anto hexadecimal string
hash_value=hashlib.sha256(data).hexdigest()
#hence we go from encode-> string to bytes sha256-> bytes to hash object and hexdigest-> hash obejct to readable hash string
with open("hash.txt","w") as hashfile:
    hashfile.writelines(path)
    hashfile.writelines("\n")
    hashfile.writelines(hash_value)
    print("hash value stored in file")

