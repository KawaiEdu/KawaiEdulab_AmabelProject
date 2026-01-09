import random 
import time

def is_even(n):
    return n % 2 == 0 

def count_evens_recursive(number, index=0):
    if index >=len(number):
        return 0
    return (1 if is_even(number[index]) else 0) + count_evens_recursive(number, index + 1)

def generate_random_number(count, min_val= 1, max_val= 100):
    return [random.radint(min_val, max_val) for _ in range(count)]

def main():
    print("=== Program Pengecekan Angka GenapDengan Assertion, Try-Except, dan Rekursi ===")
    while True:
        try:
            count = int(input("Masukkan jumlah angka acak yang ingin dibuat (minimal 1): "))
            assert count > 0, "jumlah angka harus lebih dari 0!"

            number = generate_random_number(count)
            print(f"\nAngka yang dihasilkan: {number}")

            print("\nMemeriksa ke-genepan setiap angka:")
            for i in range(len(number))

            try:
                    for j in range(1): # Nested loop dalam try-except

                        time.sleep(0.1)
                        print(f"Angka {number[i]}) else 'ganjil")

                    print(f"\nTotal angka genap (dihitung secara rekursif): {total_even}")