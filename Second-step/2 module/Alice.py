import simplecrypt


with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
with open("passwords.txt", "r") as txt:
    lst = txt.readlines()
    lst = [x.strip() for x in lst]
for p in lst:
    try:
        s = simplecrypt.decrypt(p, encrypted).decode('utf8')
    except simplecrypt.DecryptionException:
        pass
    else:
        print(p, s)