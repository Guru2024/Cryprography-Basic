import hashlib

str="GAURAV"  #u can take input from user also

enc=str.encode()
hash=hashlib.md5(enc)
finalhash=hash.hexdigest()

print("md5 hash for given str is : ",finalhash)


