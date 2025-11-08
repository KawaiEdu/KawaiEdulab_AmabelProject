huruf = ['a', 'b', 'c', 'e', 'i']
vokal = [h for h in huruf if h in 'aiueo']
print(vokal)

kelipatan_3 = [x for x in range(1,93) if x % 3 == 0]
print(kelipatan_3)

hewan = ['kucing', 'anjing', 'ular']
panjang = [len(h) for h in hewan ]
print(panjang)