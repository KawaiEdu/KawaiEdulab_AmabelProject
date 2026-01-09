kelas = {
    "kelas A": ["Tata", "abel"],
    "kelas B": ["mita", "nailong"]
}

for nama_kelas, siswa in kelas.items():
    print(nama_kelas + ":")
    for s in siswa:
        print("- " + s)
    print()