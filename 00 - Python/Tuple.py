# Mirip seperti list, tapi data yg telah dimasukkan tidak akan bisa diubah lagi dan menggunakan tanda ()

## Cara menulis tuple
# dengan ()
tuple_kurung = ('ayam','babi')
tuple_tanpa_kurung = 'ayam','sapi'
tuple_dgn_fungsiTuple = tuple(['Lulus','Tidak'])

# tuple kosong
tuple()

# Tuple tunggal
#tuple(10,) #harus diberi tanda koma

# Cara mengambil nilai tuple
tuple_kelamin = ('Laki-laki','Perempuan')
print(tuple_kelamin[0])
print(tuple_kelamin[1])
print(tuple_kelamin[-2])
print(tuple_kelamin[-1])

# Slicing tuple
print('\n' + '===' + 'Slicing' + '===' + '\n')
tuple_buah = ('apel','duren','sawi','mangga')
print(tuple_buah)
print(tuple_buah[1:3])
print('\n' + '===' + 'Slicing tanpa batas' + '===' + '\n')
print(tuple_buah[0:])
print(tuple_buah[1:])


# Sequnce Unpacking = Mengekstrak tuple ke setiap variabel masing-masing
print('\n' + '===' + 'Sequence' + '===' + '\n')

tuple_identitas = ("Haiqal",20,'islam')

nama,usia,agama = tuple_identitas

print('Nama : ',nama)
print('Usia : ',usia)
print('Agama : ',agama)

# Menggabungkan tuple
print('\n' + '===' + 'Menggabungkan' + '===' + '\n')

a = (1,2)
b = (3,4,5)
c = a + b
print(c)


"""
Operator bawaan tuple :
max() untuk mencari nilai terbesar
min() untuk mencari nilai terkecil
len() untuk mengetahui ada berapa data
"""
print('\n' + '===' + 'Operator' + '===' + '\n')
nilai = (100,90,10,30,45)
print(nilai)

max(nilai)
print(f'Nilai terbesar : {max(nilai)}')

min(nilai)
print('Nilai terkecil : ',min(nilai))

len(nilai)
print('Jumlah data : ',len(nilai))

# Sets {} / himpunan
data_sets = {1,2,3,4,5}
print(data_sets)