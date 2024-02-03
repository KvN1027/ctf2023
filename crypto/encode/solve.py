#!/usr/bin/env python3
from pwn import *

def meowmeow_decode(meowmeow_string):
    if len(meowmeow_string) != 8:
        raise ValueError("Input string must be 8 characters long")

    binary_string = ""
    meow = "meowmeow"
    for i in range(8):
        if meowmeow_string[i].isupper():
            binary_string += '1'
        elif meowmeow_string[i].islower():
            binary_string += '0'
        else:
            raise ValueError("Invalid character in meowmeow string")

    byte = int(binary_string, 2)
    return chr(byte)


r = remote("127.0.0.1", 20000)

enc = r.recvline().decode()
print(enc)

for i  in enc.split() :
    print(meowmeow_decode(i),end='')







