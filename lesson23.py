def diskon(harga, persen):
    potongan = harga * persen / 100
    return harga - potongan

print(diskon(100000, 20))

def halo(nama='Siswa'):
    if nama == 'Siswa':
        print("Halooo! selamat datang peserta belajar python")
    else:
        print(f"halo, {nama}!")

halo("Abel")
halo()

def perkalian(a, b = 2):
    return a * b

print(perkalian(4))
print(perkalian(4, 5))
    