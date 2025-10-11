angka1 =  int(input("Masukkan angka: "))
angka2 =  int(input("Masukkan angka: "))

if angka1 % 2 == 0 and angka2 % 2 == 0:
    print(f"{angka1} {angka2} adalah angka genap.")
else:
    print(f"{angka1} {angka2} adalah angka ganjil.")

modulus = angka1 % angka2

print("Hasil modulus:", modulus)