# If nya
# Kondisinya
# Aksinya

nama = input('Siapa nama anda ? = ')

# Program sebelumnya
# if kondisi : aksi
# program selanjutnya

# Program if inline
if nama == "haiqal" : print("Halo")
print(f"Terima kasih {nama}")

# Program if indentation (banyak dipakai)
if nama == "haiqal":
        print("Halo juga")
        print("sss")
print(f"Terima kasih {nama}")

# Else statement
if nama == "amanda":
    print("Bisa")
else:
    print("harus amanda")

print("Selesai")


bil = int(input("Masukan Bilangan :"))

if bil % 2 == 0:
    print(" %d Merupakan Bilangan Genap" % bil)
else:
    print("%d Merupakan Bilangan Ganjil" % bil)
