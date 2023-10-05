from pwn import *

r = remote("104.199.156.82",8101)

for i in range(100) :
    blank = r.recvuntil(b"number = ")
    numbers = r.recvline().decode()
    answer = int(''.join(sorted(str(numbers), reverse=True)))
    r.sendlineafter('answer = ',str(answer).encode())


r.interactive()
