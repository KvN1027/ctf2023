# coding:utf8
import os
from Crypto.Cipher import AES
import requests
from pwn import *
r = remote("127.0.0.1", 20000)

def queryFactors(n):
	s=[]
	url="http://factordb.com/api?query="+str(n)
	r = requests.get(url)
	factors=r.json()['factors']
	for f in factors:
		for i in range(f[1]):
			s.append(int(f[0]))
	return s

e = int(r.recvline().strip().partition(b' = ')[2].decode())
n = queryFactors(r.recvline().strip().partition(b' = ')[2].decode())
c = int(r.recvline().strip().partition(b' = ')[2].decode())
p,q = n[0],n[1]

# 计算d
def egcd(a, b):
  if a == 0:
    return (b, 0, 1)
  else:
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

d = egcd((p - 1) * (q - 1), e)[2]
if d < 0:
    d += (p - 1) * (q - 1)

m = hex(pow(c,d,p*q))[2:]
print(bytes.fromhex(m))

