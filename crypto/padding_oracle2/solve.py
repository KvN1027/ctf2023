#!/usr/bin/env python3
from pwn import *

def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

r = remote("127.0.0.1", 20000)

enc = bytes.fromhex(r.recvline(keepends=False).decode())
print(enc)
def oracle(c):
    r.sendline(c.hex())
    status = r.recvline()
    if status == b"Well received :)\n":
        return True
    else:
        return False

flag = b""

for i in range(16, len(enc), 16):
    ans = b''
    iv, block = bytearray(enc[i-16:i]), enc[i:i+16] 
    print("origin IV:",iv)
    for j in range(16): 
        for k in range(256):
            if oracle(iv[:16-1-j] + bytes([k]) + xor(bytes(list(range(1,j+1))), xor(iv[-j:], ans)) + block):
                ans = bytes([iv[16-1-j] ^ k ^ (0x00)]) + ans
                print(ans)
                break
    flag += ans




