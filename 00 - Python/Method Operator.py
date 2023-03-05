# Operator dalam bentuk method
## Merubah case dari string

# Merubah semua ke uppercase
salam = "woi!"
print("normal = " ,salam)
salam = salam.upper()
print('upper = ',salam)

# Merubah ke lowercase
sapaan = "HaLo aKKu AmaNda"
print('normal ='+ sapaan)
sapaan = sapaan.lower()
print('lower =' + sapaan)

# pengecekan dengan isX method

## Contoh untuk pengecekan lowercase
salam = "sist"
apakah_lower = salam.islower() # hasilnya bool
print(salam + ' apakah lower ? ' + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya bool
print(salam + ' apakah upper ? ' + str(apakah_upper))

# isalpha() ; untuk mengecek semuanya huruf
# isalnum() ; huruf dan angka
# isdecimal() ; angka saja
# isspace() ; spasi, tab, newline \n
# istittle() ; semua kata dimulai dengan huruf besar

contoh1 = 'Aku lahir 4 november'
apakah_SemuaHuruf = contoh1.isalpha()
print(contoh1 + ' huruf semua ? ' + str(apakah_SemuaHuruf))

contoh2 = 'aku umur tahun'
bener_ga = contoh2.isalnum()
print(contoh2 + ' ada huruf sama angka ga ? ' + str(bener_ga))

contoh3 = '20'
huruf_semua = contoh3.isdecimal()
print(contoh3 + ' huruf semua ? ' + str(huruf_semua))

contoh4 = 'ada spasi?'
ada_spasi = contoh4.isspace()
print(contoh4 + ' ada spasi ? ' + str(ada_spasi))

contoh5 = 'The Legend Of Aang'
judul = contoh5.istitle()
print(contoh5 + ' bener ga ? ' + str(judul))

# Ngecek komponen startswith() dan endswith()
cek = "Amanda Haiqal".startswith("Amanda")
print('cek = ' + str(cek))

cek1 = "Amanda Haiqal".endswith('Haiqal')
print('cek = ' + str(cek1))

# Penggabungan komponen join() split()
join = ['aku','sayang','kamu']
print(join)

join1 = ','.join(join)
print(join1)

gabungan  = ' '.join(join)
print(gabungan)

gabung = 'akurrsayangrrkamu'
print(gabung.split('rr'))

# Alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(10)
print("'"+tengah+"'")

tengah = "tengah".center(20,"=")
print("'"+tengah+"'")

# kebalikannya strip()
tengah = tengah.strip("=")
print("'"+tengah+"'")

kanan = "kanan".strip()
print("'"+kanan+"'")

kiri = "kiri".strip()
print("'"+kiri+"'")