# continue, pass, break

# pass ( berfungsi dummy, tidak akan dieksekusi)

angka = 0
#while angka < 5:
#   angka += 1
#   if angka == 3:
#      pass # ini tidak akan dieksekusi
#print(angka)
#print("Program 1")

# continue
print(f"angka sekarang = {angka}")

while angka <5 :
    angka += 1
    print(f'angka sekarang = {angka}') # aksi 1

    if angka == 3:
        print("selanjutnya 3")
        continue # akan membuat loop meloncat ke step selanjutnya
    print("lanjut") #aksi 2

print("Berhenti")
