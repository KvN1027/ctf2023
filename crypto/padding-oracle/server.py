#!/usr/bin/env python3
import os
from Crypto.Cipher import AES

KEY = os.urandom(16)
IV = os.urandom(16)
FLAG = open('./flag', 'rb').read()

def pad(data):
    p = 16 - len(data) % 16
    return data + bytes([p]) * p

def unpad(data):
    if not all([x == data[-1] for x in data[-data[-1]:]]):
        raise ValueError
    return data[:-data[-1]]

def main():
    aes = AES.new(KEY, AES.MODE_CBC, IV)
    cipher = aes.encrypt(pad(FLAG))
    print('send "1" to get message , send "2" to talk!')
    

    while True:
        ip = input('mode = ')
        if ip == "1" :
            print(f"msg = {(IV + cipher).hex()}")
        if ip == "2" :
            cipher = bytes.fromhex(input('talk = ').strip())
            iv, cipher = cipher[:16], cipher[16:]
            try:
                aes = AES.new(KEY, AES.MODE_CBC, iv)
                plain = unpad(aes.decrypt(cipher))
                print('server_res_status = 200')
            except ValueError:
                print('server_res_status = 500')
        print("======")

try :
    main()
except:
    print("program error!")