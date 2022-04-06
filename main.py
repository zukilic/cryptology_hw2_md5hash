#Zeynep Ülkü Kılıç
#Homework2
#Question2

'''
Programda her bir karakter teker teker değiştirilip toplam 501 adet hash kodu oluşturulmuştur.
Birbirleriyle aynı olan ya da en ufak bir benzerliği olan hash kodu çıkmamıştır.
'''

import hashlib

# initializing string
str2hash = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

hash_code = []

# sending to md5()
result = hashlib.md5(str2hash.encode())
hash_code.append(result.hexdigest())

new = list(str2hash)

for i in range(len(str2hash)):
    new[i] = "b"
    str2hash = "".join(new)
    result = hashlib.md5(str2hash.encode())
    hash_code.append(result.hexdigest())

for i in range(len(hash_code)):
    print(hash_code[i])
