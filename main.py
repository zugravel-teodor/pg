import random
lo = "abcdefghijklmnopqrstuvwxyz"
up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nu = "0123456789"
sy = "!@#$%^&*()_+{}[]|:;?<>,.~`/"
ch = lo + up + nu + sy
le = int(input("len: "))
pa = "".join(random.choices(ch, k=le))
print(pa)