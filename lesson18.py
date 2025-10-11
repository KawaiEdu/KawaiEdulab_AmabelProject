def kalkulator():
    try:
        angka1 = float(input("masukan angka pertama ")) 
        angka2 = float(input("masukan angka ke dua "))
        operasi = input("masukan operasi (+, -, *, /) ")

        if operasi == "+":
            hasil = angka1 + angka2
        elif operasi == "-":
            hasil = angka1 - angka2
        elif operasi == "*":
            hasil = angka1 * angka2
        elif operasi == "/":
            hasil = angka1 / angka2
        else :
            print("operasi tidak valid")
        
        return print(f"hasil: {hasil}")
    
    except ValueError: 
        print("input harus angka")

    except ZeroDivisionError:
        print("tidak bisa dibagi angka nol")

while True:
    print("\nKalkulator Sederhana")
    kalkulator()
    lagi = input("apakah anda ingin menghitung lagi? (ya/tidak): ")

    if lagi.lower() != "ya":
        print("Thank you! and goodbye for now")
        break