import os

from base64 import b64encode, b64decode 
from Crypto.Cipher import AES

flag = open('flag', 'r').read() 
key = os.urandom(16)
myiv = os.urandom(16)
msg = b'A'*16+b'admin=0'+b'A'*7 #00

def pad(data):

    k =-len(data) % 16 
    if k==0: k=16
    return data + bytes([k] * k)

def unpad(data):
    return data[:-data[-1]]

def encrypt(data): 
    aes = AES.new(key, AES.MODE_CBC, iv = myiv) 
    return aes.encrypt(pad(data))

def decrypt(data):
    redata = data
    aes = AES.new(key, AES.MODE_CBC, iv = myiv) 
    return unpad(aes.decrypt(redata))

def  main():
    print('AES+CBC = magic !')
    print('cookieinfo = ',msg)
    print('magic = ',b64encode(encrypt(msg)).decode())
    print('====================================================')
    print()
    cipher = b64decode(input("your magic = ").strip()) 
    if b'admin=1' in decrypt(cipher): 
        print(flag)



try: 
    main()
except:
    print("m@g1c err0r @.@")