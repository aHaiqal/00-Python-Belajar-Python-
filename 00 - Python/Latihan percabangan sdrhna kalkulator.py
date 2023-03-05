# Kalkulator sederhana
print(10*"=")
print("Kalkulator")
print(10*"="+"\n")

angka_1 = float(input("Masukkan : "))
operator = input("operator (+,-,x,/) : ")
angka_2 = float(input("Masukkan : "))

# Percabangan
if operator == "+" :
    hasil = angka_1 + angka_2
    print(f"hasilnya {hasil}")
elif operator == "-" :
    hasil = angka_1 - angka_2
    print(f"hasilnya {hasil}")
elif operator == "*" or operator == "x":
    hasil = angka_1 * angka_2
    print(f"hasilnya {hasil}")
elif operator == "/" :
    hasil = angka_1 / angka_2
    print(f"hasilnya {hasil}")
else:
    print("Ulang")

print("Akhir dari program")