#!/usr/bin/env python3
from pwn import *

def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

r = remote("127.0.0.1", 20000)

r.sendlineafter(b"mode = ","1".encode())

enc = bytes.fromhex(r.recvline().strip().partition(b'msg = ')[2].decode())
print(enc)
def oracle(c):
    r.sendlineafter('mode = ', "2".encode())
    r.sendlineafter('talk = ', c.hex())
    status = r.recvline()
    r.recvline() 
    if b'200' in status:
        return True
    else:
        return False

flag = b''
for i in range(16, len(enc), 16):
    ans = b''
    iv, block = enc[i-16:i], enc[i:i+16] 
    print("origin IV:",iv)
    for j in range(16): 
        for k in range(256): 
            if j == 0 and k == iv[15]:
                continue
            if oracle(iv[:16 - 1 - j] + bytes([k]) + xor(bytes([j + 1] * j), xor(iv[-j:], ans)) + block):
                ans = bytes([iv[16 - 1 - j] ^ k ^ (j + 1)]) + ans
                print(ans)
                break
    flag += ans





print(flag)





