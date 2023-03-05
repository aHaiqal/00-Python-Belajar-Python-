# Break

angka = 0

while True:
    angka += 5
    print(f"Angka sekarang = {angka}")
    if angka == 50:
        print("udah 50")
        break
    print("lanjut")
print("Cukup")

# Perintah Baru
print("\n"+"Perintah Baru"+"\n")

data_int = int(input("Hitung sampai = "))
angka = 0

while True:
    angka += 1
    print(f"count = {angka}")

    if angka == data_int:
        print("Sip")
        break

    print("lanjut")

print("Cukup")
