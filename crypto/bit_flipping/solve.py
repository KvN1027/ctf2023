#!/usr/bin/env python3
import string
from pwn import *
from base64 import *

def xor(a,b) :
    return bytes([x^y for x, y in zip(a,b)])

r = remote('127.0.0.1', 20000)
r.recvuntil('magic = ')
cipher = b64decode(r.recvline().strip())
print(cipher)

flag = bytearray(cipher)
flag[:7] = xor(xor(b'admin=0',flag[:7]), b'admin=1')

print(bytes(flag))

r.sendlineafter('your magic = ',b64encode(bytes(flag)))
r.interactive()