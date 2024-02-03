#!/usr/bin/env python3
import os
from Crypto.Cipher import AES

KEY = os.urandom(16)
FLAG = open('./flag').read()

def pad(m):
    padlen = -len(m) % 16
    return m + bytes([0] * padlen)

def main():
    aes = AES.new(KEY, AES.MODE_ECB)
    
    # encrypt token
    user = input('user = ').strip()
    if '&' in user:
        raise ValueError

    token = f'user={user}&role=guest&'.encode()


    token = aes.encrypt(pad(token))
    print(f'cookie = {token.hex()}')
    
    # decrypt token
    token = bytes.fromhex(input('cookie = ').strip())
    token = aes.decrypt(token)
    user, role, _ = token.split(b'&')
    if role.split(b'=')[1] == b"guest" :
        print(f'i\'m still the same')
    else:
        print(FLAG)
        

try:
    main()
except:
    print("error@@")