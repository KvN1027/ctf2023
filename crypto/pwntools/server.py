#!/usr/bin/env python3
import os
import random

KEY = os.urandom(16)
flag = open('./flag').read()

def pad(m):
    padlen = -len(m) % 16
    return m + bytes([0] * padlen)

def main():
    print("""
<<<================================>>>
EASY CRYPTO MINER v1.0
rule:
example:  143554
help me sort the number like :554431

example2: 855943
help me sort the number like :985543

solve 1 number to get 1 point
win a flag by 100 point !
<<<================================>>>
""")
    point = 0
    

    while 1 :
        key = random.randrange(100000,1000000)
        number = key
        sorted_number = int(''.join(sorted(str(number), reverse=True)))
        print(f'number = {key}')
        while 1 :
            ip = int(input("answer = "))
            if ip == sorted_number :
                point += 1
                print("correct! point:",point,end="\n\n")
                break
        if point >= 100 :
            print(flag)
            break

try:
    main()
except:
    print("error@@")