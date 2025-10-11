kamus_buah = {
    "apel": "buah warna merah",
    "pisang": "buah warna kuning",
    "melon": "buah warna ijo"
}

buah = input("masukkan nama buah")
if buah in kamus_buah:
    print(f"{buah}: {kamus_buah[buah]} ")
else:
    print(f"buah tidak ada dalam kamus.")