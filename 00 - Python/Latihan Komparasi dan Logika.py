# Membuat gabungan area rentang dari angka

# +++++3-------10++++++

inputUser = float(input("Masukkan angka yang bernilai\nkurang dari 3 \natau\nlebih dari 10\n:"))

# +++3---
# Memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 =", isKurangDari)

# ----10++++
# Memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =", isLebihDari)

# +++++3-------10++++++
isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukan: ", isCorrect)

# ----3++++10----
# Kasus irisan
print("\n",10*"=","\n")
inputUser = float(input("Masukkan angka yang bernilai\nlebih dari 3 \ndan\nkurang dari 10\n:"))

# ----3++++
# Lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3 = ",isLebihDari)
# +++++10----
isKurangDari = inputUser < 10
print("Kurang dari 3 = ",isKurangDari)

isCorrect = isKurangDari and isLebihDari
print("Angka yang anda masukan: ", isCorrect)


# Latihan
x=float(input("masukkan angka > 0 dan < 5 atau > 8 dan < 11 : "))
print(0<x<5 or 8<x<11)

x=float(input("masukkan angka < 0 atau >5 dan <8 atau >11 : "))
print(x<0 or 5<x<8 or 11<x )