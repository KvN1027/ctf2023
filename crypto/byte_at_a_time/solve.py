#!/usr/bin/env python3
import string
from pwn import *

r = remote('127.0.0.1', 20000)

def oracle(m):
    r.sendlineafter('say...my...name... = ', m.hex())
    tmp = r.recvline().strip().decode()
    return bytes.fromhex(tmp)

flag = b''
for i in range(19):
    prefix = b'A' * (32 - 1 - i)
    target = oracle(prefix)[:32] #target = X個A+flag流進來Y個字
    for c in string.printable:
        test = oracle(prefix + flag + bytes([ord(c)]))[:32]
        if test == target:
            flag += bytes([ord(c)])
            print(flag)
            break

r.interactive()