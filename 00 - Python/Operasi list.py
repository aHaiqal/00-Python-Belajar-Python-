# Mengubah isi dari list
list_buah = ['nanas','mangga','stoberi','apel']
print(list_buah)

list_buah [1] = 'rambutan'
print(list_buah)

list_buah [0:3] = ['naga','pepaya']
print(list_buah)

# Menambah list dari belakang
list_buah.append('ayam')
print(list_buah)

# Menambah list di depan atau mana pun
list_buah.insert(1,'sapi') # 1 letaknya, sapi datanya
print(list_buah)

# Menghapus data list belakang 
list_angka = [1,2,3,4,5]
print(list_angka)

angka_dihapus = list_angka.pop()

print('angka dihapus : ', angka_dihapus)
print(list_angka)

# Menghapus dengan remove(), sesuai dengan apa yg kita input
list_angka1 = [1,2,3,4,5,6]
print(list_angka1)

list_angka1.remove(4)
print(list_angka1)

# Menghapus dengan del (menghapus berapa pun dari list)
list_barang = ['kasur','bantal','guling','sprei']
print(list_barang)
del list_barang[0:3]
print(list_barang)

list_barang1 = ['kasur','bantal','guling','sprei']
print(list_barang1)
del list_barang1[1:2]
print(list_barang1)

# Menggabungkan list
buah = ['apel','mangga']
angka = [1,2]
bool = [True,False]

gabung = buah + angka + bool
print(gabung)

# Mengurutkan list
## Menggunakan .sort() {mengurutkan data sesuai urutan}
data_buah = ['durian','nanas','apel','jeruk']
print(data_buah)

data_buah.sort()
print(data_buah)

## Menggunakan .reverse()
data_buah.reverse()
print(data_buah)

# Menghitung data
data_angka = [1,2,3,1,2,3,1,2,35,3,4,5]
jumlah_2 = data_angka.count(2)
print(f'Jumlah angka : {jumlah_2}')

# Ambil posisi data
indeks = data_angka.index(35)
print(f'Posisi angka 35 : {indeks}')