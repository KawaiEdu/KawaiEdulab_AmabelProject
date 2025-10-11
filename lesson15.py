daftar_belanja = set()

while True:
    item = input("masukan item belanja yang ingin ditambahkan ")
    if item.lower() == "selesai" :
        print("keluar dari program")
        break
    daftar_belanja.add(item)

print("daftar belanja anda")
for item in daftar_belanja :
    print(f"-{item}")