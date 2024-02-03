#!/usr/bin/env python3
import os
import string
FLAG = open('./flag', 'r').read()

def meowmeow_encode(byte):

    binary_string = bin(byte)[2:].zfill(8)
    meow  = "meowmeow"
    meowmeow = ""
    
    for bit in range(8) :
        if binary_string[bit] == '0' :
            meowmeow += meow[bit]
        else :
            meowmeow += meow[bit].upper()

    return meowmeow 


def main() : 
    res = ''
    for i in FLAG :
        res += meowmeow_encode(ord(i)) + ' '
    print(res)

try :
    main()
except:
    print("program error!")