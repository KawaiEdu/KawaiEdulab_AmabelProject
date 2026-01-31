class Hewan:
    def __init__(self, nama, jenis, suara):
        self.nama = nama
        self.jenis = jenis 
        self.suara = suara

    def bergerak(self):
        return f"{self.nama} sedang bergerak"
    
    def bersuara(self):
        return f"{self.nama} bersuara: {self.suara}"
    
class Manusia:
    def __init__(self, nama, umur, pekerjaan):
        self.nama = nama
        self.umur = umur
        self.pekerjaan = pekerjaan

    def perkenalan(self):
        return f"Haloo, nama saya {self.nama}, umur {self.umur} tahun, bekerja sebagai {self.pekerjaan}."
        
    def bekerja(self):
        return f"{self.nama} sedang bekerja sebagai {self.pekerjaan}."
    
class Benda:
    def __init__(self, nama, fungsi, bahan):
        self.nama = nama
        self.fungsi = fungsi
        self.bahan = bahan

    def deskripsi(self):
        return f"{self.nama} terbuat dari {self.bahan} digunakan untuk {self.fungsi}."
    
def main():
    print("\n=== input Data Hewan ===")
    nama_hewan = input("masukkan nama hewan:")
    jenis_hewan = input("masukkan jenis hewan:")
    suara_hewan = input("masukkan suara hewan:")
    hewan1 = Hewan(nama_hewan, jenis_hewan, suara_hewan)

    print("\n=== input Data Manusia ===")
    nama_Manusia = input("masukkan nama manusai:")
    umur_Manusia = input("masukkan umur manusia:")
    pekerjaan_Manusia = input("masukkan pekerjaan manusia:")
    Manusia1 = Manusia(nama_Manusia, umur_Manusia, pekerjaan_Manusia)

    print("\n=== input Data Benda ===")
    nama_Benda = input("masukkan nama benda:")
    fungsi_Benda = input("masukkan fungsi benda:")
    bahan_Benda = input("masukkan bahan benda:")
    Benda1 = Benda(nama_Benda, fungsi_Benda, bahan_Benda)
    
    while True:
        print("\n=== MENU PROGRAM ===")
        print("1. Tampilkan aktivitas Hewan")
        print("2. Tampilkan aktivitas Manusia")
        print("3. Tampilkan deskripsi Benda")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan (1-4): ")
        if pilihan == "1":
            print(hewan1.bergerak())
            print(hewan1.bersuara())
        elif pilihan == "2":
            print(Manusia1.perkenalan())
            print(Manusia1.bekerja())
        elif pilihan == "3":
            print(Benda1.deskripsi())
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()