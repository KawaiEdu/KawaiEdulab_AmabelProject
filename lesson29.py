class Siswa:
    def __init__(self, nama, kelas):
        self.nama = nama; self.kelas = kelas
        self.nilai = []

    def tambah_nilai(self, x):
        if 0 <= x <= 100: self.nilai.append(x)

    def rata(self):
        return sum(self.nilai)/len(self.nilai) if self.nilai else 0
    
    def rangkuman(self):
        return f"{self.nama} ({self.kelas}) — Rata: {self.rata():.1f}"

a = Siswa("Amabel","8i")
a.tambah_nilai(90); a.tambah_nilai(95)
print(a.rangkuman())