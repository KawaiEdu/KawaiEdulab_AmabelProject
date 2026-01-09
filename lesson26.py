def faktorial(n):
    if n <=1: return 1
    return n * faktorial(n-1)

def jumlah(n):
    if n == 0: return 0
    return n + jumlah(n-1)

def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

while True:
    print("\\n[1] Faktorial [2] Fibonacci [3] Jumlah 1..n [0] keluar")
    p = input("Pilih: ")
    if p == "0": break
    n = int(input("n: "))
    if p == "1": print("hasil:", faktorial(n))
    if p == "2": print("Hasil:", fib(n))
    elif p == "3": print("Hasil:", jumlah(n))