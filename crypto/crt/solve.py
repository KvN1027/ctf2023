from Crypto.Util.number import long_to_bytes,bytes_to_long

# copy from the output of server.py
hint = []
muls = []
mods = []

from functools import reduce
def egcd(a, b):

    if 0 == b:
        return 1, 0, a
    x, y, q = egcd(b, a % b)
    x, y = y, (x - a // b * y)
    return x, y, q

def chinese_remainder(pairs):

    mod_list, remainder_list = [p[0] for p in pairs], [p[1] for p in pairs]
    mod_product = reduce(lambda x, y: x * y, mod_list)
    mi_list = [mod_product//x for x in mod_list]
    mi_inverse = [egcd(mi_list[i], mod_list[i])[0] for i in range(len(mi_list))]
    x = 0
    for i in range(len(remainder_list)):
        x += mi_list[i] * mi_inverse[i] * remainder_list[i]
        x %= mod_product
    return x

print(long_to_bytes(chinese_remainder([ (mods[i] , (hint[i] * pow(muls[i],-1,mods[i])) % mods[i]  ) for i in range(20) ])))