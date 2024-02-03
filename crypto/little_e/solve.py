import gmpy2
from pwn import *

r = remote("127.0.0.1", 20000)

r. recvuntil(b'meow')
ans = b''
while 1 :
    token = r.recvline().strip().partition(b' = ')[2].decode()
    if token == b'meow meow bye bye':
        break
    r.sendline('123')
    step = int(token)
    (t1, t2) = gmpy2.iroot(step, 3)
    ans = ans + int(t1).to_bytes(1, 'big') 
    print(ans)