from Crypto.Util.number import bytes_to_long, getPrime
flag =  open('./flag',"rb").read()

secret = bytes_to_long(flag)
mods = [ getPrime(20) for i in range(20)]
muls = [ getPrime(20) for i in range(20)]

hint = [secret * muls[i] % mods[i] for i in range(20)]

print(f"hint = {hint}")
print(f"muls = {muls}")
print(f"mods = {mods}")