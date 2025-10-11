daftar_belanja = [] # ini adalah Daftar Belanja yang akan di pilih

while True:
   print("\nDaftar Belanja:",daftar_belanja)
   print("1. Tambah item")
   print("2. Hapus item")
   print("3. Copy")
   print("4. extend")
   print("5. keluar")
   choice = int(input("pilih opsi(1/2/3): "))
   
   if choice == 1:
      item = input("masukkan item yang ingin di masukkan: ")
      daftar_belanja.append(item)
   elif choice == 2: 
      item = input("Masukan item yang ingin dihapus")
      if item in daftar_belanja:
         daftar_belanja.remove(item)
      else:
         print("item tidak di temukan dalam daftar!")
   elif choice == 3:
      daftar_belanjanya = daftar_belanja.copy()
      print(daftar_belanjanya) # output: ["bahan-bahan untuk makanan", "kebutuhan lain nya"]
   elif choice == 4 :
      buah = ["melon", "anggur"]
      sayur = ["sawi", "kangkung"]
      buah.extend(sayur)
      print(buah) # output : ["melon", "anggur", "sawi", "kangkung"]
   elif choice == 5:
      print("Terimakasih telah menggunkan progam ini")
      break