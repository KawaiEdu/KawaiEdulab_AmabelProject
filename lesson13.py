Holiday = ("sabtu", "minggu")

activities_Holiday = ("jalan-jalan", "istirahat")
activities = input("masukkan aktivitas yang ingin di pilih")
day = input("masukkan hari ")

if day in Holiday:
    print(f"{day} adalah hari libur!")
else: 
    print(f"{day} hari masuk!")

if activities in activities_Holiday:
    print(f"{activities} itu adalah aktifitas di hari libur!")
else:
    print(f"{activities} itu bukan aktifitas! tetapi kegiatan yg di lakukan tiap hari")