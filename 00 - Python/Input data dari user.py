# Data yang dimasukkan pasti string
data = input("Masukkan data: ")

print("data = ",data,",type =",type(data))

# Jika ingin mengambil int dan float, maka :
angka = int(input("Masukkan angka: "))
angka = float(input("Masukkan angka: "))

print("data = ",angka,",type =",type(angka))

# Jika ingin mengambil boolean, harus ke integer dulu
biner = bool(int(input("Masukkan nilai boolean: ")))

print("data = ",biner,",type =",type(biner))