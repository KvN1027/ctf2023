import random
from Crypto.Util.number import getPrime

flag = open('./flag').read()


def generate_keypair():
    p = 10000079
    q = 10000019
    n = 100000980001501
    phi = (p - 1) * (q - 1)
    e = 3
    d = pow(e, -1, phi)

    return (e, n), (d, n)

def encrypt(plaintext, public_key):
    e, n = public_key
    m = int.from_bytes(plaintext.encode(), 'big') 
    c = pow(m, e, n)
    return c


def main():
    public_key = generate_keypair()
    print("""
           __..--''``---....___   _..._    __
 /// //_.-'    .-/";  `        ``<._  ``.''_ `. / // /
///_.-' _..--.'_    \                    `( ) ) // //
/ (_..-' // (< _     ;_..__               ; `' / ///
 / // // //  `-._,_)' // / ``--...____..-' /// / //
My cat can only speak one byte at a time
press enter to get next word
                    """)
    print(f"e = {public_key[0]}")
    print(f"n = {public_key[1]}")
    for i in flag :
        encrypted_flag = encrypt(i, public_key)
        print(f"meowsay = {encrypted_flag}")
        m = input("")
    print("meow meow bye bye!")


if __name__ == "__main__":
    main()