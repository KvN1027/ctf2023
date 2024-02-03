import random
from Crypto.Util.number import getPrime

flag = open('./flag').read()

def generate_keypair():
    p = 169524110085046954319747170465105648233168702937955683889447853815898670069828343980818367807171215202643149176857117014826791242142210124521380573480143683660195568906553119683192470329413953411905742074448392816913467035316596822218317488903257069007949137629543010054246885909276872349326142152285347048927
    q = 170780128973387404254550233211898468299200117082734909936129463191969072080198908267381169837578188594808676174446856901962451707859231958269401958672950141944679827844646158659922175597068183903642473161665782065958249304202759597168259072368123700040163659262941978786363797334903233540121308223989457248267
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    d = pow(e, -1, phi)

    return (e, n), (d, n)


def encrypt(plaintext, public_key):
    e, n = public_key
    m = int.from_bytes(plaintext.encode(), 'big')  
    c = pow(m, e, n)
    return c

def decrypt(ciphertext, private_key):
    d, n = private_key
    m = pow(ciphertext, d, n)
    return m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()  



def main():
    public_key, private_key = generate_keypair()
    encrypted_flag = encrypt(flag, public_key)
    print(f"e = {public_key[0]}")
    print(f"n = {public_key[1]}")
    print(f"c = {encrypted_flag}")

if __name__ == "__main__":
    main()
