import hashlib

str="GAURAV"

enc=str.encode()

hash=hashlib.sha1(enc)
print("sha1 hash for str is : ",hash.hexdigest()+"\n")

hash=hashlib.sha224(str.encode())
print("sha224 hash for str is : ",hash.hexdigest()+"\n")


hash=hashlib.sha256(str.encode())
print("sha256 hash for str is : ",hash.hexdigest()+"\n")


hash=hashlib.sha384(str.encode())
print("sha384 hash for str is : ",hash.hexdigest()+"\n")

hash=hashlib.sha512(str.encode())
print("sha512 hash for str is : ",hash.hexdigest()+"\n")


