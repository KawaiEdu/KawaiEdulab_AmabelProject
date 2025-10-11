tambah = lambda x, y: x + y
kurang = lambda x, y: x - y
kali = lambda x, y: x * y
bagi = lambda x, y: x / y

while True:
    print("Selamat datang di Kalkulator Lambda!")
    x = float(input("Masukkan angka pertama: "))
    y = float(input("Masukkan angka kedua: "))
    operasi = input("Pilih operasi (+, -, *, /): ")

    if x != 0 or y != 0:
        if operasi == '+':
            print("Hasil: ", tambah(x, y))
        elif operasi == '-':
            print("Hasil: ", kurang(x, y))
        elif operasi == '*':
            print("Hasil: ", kali(x, y))
        elif operasi == '/':
            print("Hasil: ", bagi(x, y))
        else:
            print("Operasi tidak valid!")
    else:
        print("Error! Tidak bisa dibagi dengan 0")