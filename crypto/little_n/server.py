import random
from Crypto.Util.number import getPrime

# 生成 RSA 密鑰
def generate_keypair():
    # 選擇兩個隨機的質數 p 和 q
    p = 169524110085046954319747170465105648233168702937955683889447853815898670069828343980818367807171215202643149176857117014826791242142210124521380573480143683660195568906553119683192470329413953411905742074448392816913467035316596822218317488903257069007949137629543010054246885909276872349326142152285347048927
    q = 170780128973387404254550233211898468299200117082734909936129463191969072080198908267381169837578188594808676174446856901962451707859231958269401958672950141944679827844646158659922175597068183903642473161665782065958249304202759597168259072368123700040163659262941978786363797334903233540121308223989457248267
    n = p * q
    phi = (p - 1) * (q - 1)

    # 選擇一個公開指數 e，確保它和 phi 互質
    e = 65537

    # 計算私鑰 d
    d = pow(e, -1, phi)

    return (e, n), (d, n)

# 加密明文
def encrypt(plaintext, public_key):
    e, n = public_key
    m = int.from_bytes(plaintext.encode(), 'big')  # 將文字轉換為整數
    c = pow(m, e, n)
    return c

# 解密密文
def decrypt(ciphertext, private_key):
    d, n = private_key
    m = pow(ciphertext, d, n)
    return m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()  # 將整數轉換為文字

# 生成隨機的 flag
def generate_flag():
    return r"flag{meow}"

# 主程式
def main():
    # 生成密鑰
    public_key, private_key = generate_keypair()

    # 生成 flag
    flag = generate_flag()

    # 加密 flag
    encrypted_flag = encrypt(flag, public_key)

    # 輸出公開金鑰和密文
    print("Public Key:")
    print(f"e = {public_key[0]}")
    print(f"n = {public_key[1]}")
    print("Encrypted Flag:")
    print(f"c = {encrypted_flag}")

if __name__ == "__main__":
    main()
