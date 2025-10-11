Celcius = int(input("masukkan suhu kedalam Celcius "))

reamur = (4/5) * (Celcius)
fahrenheit = ((9/5) * (Celcius) ) + 32
kelvin = Celcius + 273

print("\n1. Celcius")
print("2. Reamur")
print("3. fahrenheit")
print("4. kelvin")
print("5. Keluar")
choice = int(input("masukan pilihan kamu "))

if choice == 1:
    print(f"\nSuhu Celcius : {Celcius}")
elif choice == 2:
    print(f"\nSuhu Rearmur: {reamur}")
elif choice == 3:
    print(f"\nSuhu fahrenheit: {fahrenheit}")
elif choice == 4:
    print(f"\nSuhu kelvin: {kelvin}")
elif choice == 5:
    print("Program telah selesai")
       

suhu = int(input("masukkan suhu saat ini "))

if suhu < 10:
    print("Cuaca: Dingin")
    print("Saran: Pakai jaket tebal dan minum cokelat panas!")
elif suhu <=25:
    print("Cuaca: sejuk")
    print("Saran: Waktu berjalan-jalan atau olahraga ringan!")
elif suhu <=35:
    print("Cuaca: hangat")
    print("Saran: Nikmati piknik atau berenang!")
else:
    print("Cuaca: panas")
    print("saran: tetap di dalam rumah dan minum air dingin!") 