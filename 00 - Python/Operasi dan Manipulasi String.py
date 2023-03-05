# Menyambung String (Concatenate)
nama_depan = "Daffa"
nama_tengah = "D"
nama_akhir = "Mahardika"

nama_lengkap = nama_depan + nama_tengah + nama_akhir
print(nama_lengkap)

nama_lengkap = nama_depan + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)

# Menghitung panjang string
panjang = len(nama_lengkap)
print(panjang)

# Operator untuk string
## Mengecek apakah ada komponen karakter atau string di string
d = "d"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + "=" + str(status))

d = "s"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + "=" + str(status))

d = "d"
status = d not in nama_lengkap
print(d + " tidak ada di " + nama_lengkap + "=" + str(status))

d = "s"
status = d not in nama_lengkap
print(d + " tidak ada di " + nama_lengkap + "=" + str(status))

# Mengulang string
print("wk"*10)
print(16*"ha")

# Indexing
print("index ke 9 = " + nama_lengkap[9] )
print("Index ke -3 = " + nama_lengkap[-3])
print("Index dari 0 sampai 5  = " + nama_lengkap[0:5]) 
print("Index dari 0,2,3,5  = " + nama_lengkap[0:5:2])

# Item paling kecil
print("Item paling kecil = " + min(nama_lengkap))
# Item paling besar
print('Item paling besar = ' + max(nama_lengkap))

ascii_code = ord(" ")
print("Asci code untuk spasi = " + str(ascii_code))
data = 23
print("Asci code untuk 23 = " + chr(117))

# Operator dalam bentuk methode
data = "amanda haiqal"
jumlah = data.count("a")
print('Jumlah huruf a di data = ' + str(jumlah))