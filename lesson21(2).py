# lesson 21 filler

friend = []

while True:
    teman = input("siapa seseorang yang kamu kagumi?")
    if teman.lower()=="stop":
        break
    elif teman.strip():
        friend.append(teman.strip())
if not friend:
    print("daftar teman kosong")
else:
    for temen in friend:
        print(f"hai!, {temen} rahasia hati kuhh")