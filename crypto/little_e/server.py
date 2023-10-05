import random
from Crypto.Util.number import getPrime

# 生成 RSA 密鑰
def generate_keypair():
    # 選擇兩個隨機的質數 p 和 q
    p = 10000079
    q = 10000019
    n = 100000980001501
    phi = (p - 1) * (q - 1)

    # 選擇一個公開指數 e，確保它和 phi 互質
    e = 3

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



# 主程式
def main():
    # 生成密鑰
    public_key, private_key = generate_keypair()

    # 生成 flag
    flag = r'flag{i_like_u}'

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
    # 加密 flag
    for i in flag :
        encrypted_flag = encrypt(i, public_key)
        # 輸出公開金鑰和密文
        print(f"meowsay = {encrypted_flag}")
        m = input("")
    print("meow meow bye bye!")


if __name__ == "__main__":
    main()