import random
from utils import valid_int
target = random.randint(1, 20)
while True:
    raw = input("Tebak 1..20: ")
    n = valid_int(raw)
    if n is None: 
        print("Masukkan angka!"); continue
    if n == target: print("Benar!"); break
    print("Terlalu", "kecil" if n < target else "besar")
    