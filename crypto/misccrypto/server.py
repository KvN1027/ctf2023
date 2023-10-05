#!/usr/bin/env python3
import os
import random
from Crypto.Cipher import AES

secret = [b"iamadminmeowemeow",b'CVE20193730',b"0w0iamacutecat",b'CVE-2016-2107',b'ur_the_best_meow'] 
index = 0

# byte-at-a-time
KEY = os.urandom(16)
IV = os.urandom(16)
FLAG = open('./flag', 'rb').read()

def pad(m):
    padlen = -len(m) % 16
    return m + bytes([0] * padlen)

def pad2(data):
    p = 16 - len(data) % 16
    return data + bytes([p]) * p

def unpad(data):
    if not all([x == data[-1] for x in data[-data[-1]:]]):
        raise ValueError
    return data[:-data[-1]]

def baat():
    print('req = byte-at-time')
    aes = AES.new(KEY, AES.MODE_ECB)
    while True:
        message = bytes.fromhex(input('ur_test = ').strip())
        if b'secret:' in message :
            if message.split('secret:')[2] == bytes(secret[index]):
                index+=1
                break
        cipher = aes.encrypt(pad(message + secret))
        print(f'{cipher.hex()}')

def po():
    print('req = padding-oracle')
    aes = AES.new(KEY, AES.MODE_CBC, IV)
    cipher = aes.encrypt(pad2(secret[index]))
    while True:
        cipher = bytes.fromhex(input('talk = ').strip())
        if b'secret:' in cipher :
            if cipher.split('secret:')[2] == bytes(secret[index]):
                index+=1
                break
        iv, cipher = cipher[:16], cipher[16:]
        try:
            aes = AES.new(KEY, AES.MODE_CBC, iv)
            plain = unpad(aes.decrypt(cipher))
            print('200')
        except ValueError:
            print('500')



def main():
    print("""
<<<================================>>>
EASY CRYPTO MINER v2.0

Welcome 2 v2.0 !
As u know, brute-force require 
a lot of computer resources.
I'll connect u to another Server.
can u help me to crack these server?

rule:
example1:
req = padding-oracle
ur_test = <<type your test here>>

example2:
req = byte-at-time
ur_test = <<type your test here>>  

if you want to send SECRET to me:
ur_test = secret:<<type secret here>>
ps: all words hex.

solve 5 servers , 
and I will give u the flag u want
<<<================================>>>
""")

    for i in range(5) :
        if random.randint(1,2) == 2 :
            baat()
        else :
            po()
    print(FLAG)


try:
    main()
except:
    print("error@@")