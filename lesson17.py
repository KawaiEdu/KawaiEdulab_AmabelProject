def tulis_catatan():
    catatan = input("masukan catatan anda: ")
    with open("catatan.txt","a") as file:
        file.write(catatan + "\n")
        print("catatan berhasil di simpan ")

def baca_catatan():
    try:
        with open("catatan.txt", "r") as file:
            print("\nCatatan Harian Anda:")
            print(file.read())
    except FileNotFoundError:
        print("belum ada catatan yang tersimpan.")

while True:
    print("\nPilih menu.")
    print("1. Tulis Catatan")
    print("2. Baca Catatan")
    print("3. Keluar")
    pilihan = input("masukkan pilihan (1/2/3):")

    if pilihan == "1":
        tulis_catatan()
    elif pilihan == "2":
        baca_catatan()
    elif pilihan == "3":
        print("Thank you! and goodbye for now.")
        break
    else:
        print("pilihan tidak valid. silahkan coba lagi")