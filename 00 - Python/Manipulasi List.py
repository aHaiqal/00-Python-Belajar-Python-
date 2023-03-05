# Operasi

## Indeks mulai dari 0 dari depan atai -1 dari belaakng
data = ['Ucup','Otong','Dudung']

# Mengambil data dari list
data_0 = data[0]
print(f'data pertama : ', data_0)

data_terakhir = data[-1]
print(f'data terakhir : ', data_terakhir)

# Mengambil info jumlah dari data
panjang_data = len(data)
print(f'panjang dari data : {panjang_data}')


# Menambahkan data di list sesuai posisi
data.insert(1,'Asep')
print(f'Ditambahkan : {data}')

# Menambahkan di akhir list
data.append('Ipan')
print(f'diakhir : {data}')

# Menambah list dengan list
data_baru = ['Ujang','Usep']
data.extend(data_baru)
print(f'data baru : {data}')

# Merubah data
data[2] = 'Daffa'
print(f'data rubah : {data}')

# Menghapus data
data.remove('Ipan')
print(f'data hapus : {data}')

# Menghapus data paling belakang
data.pop()
print(f'data baru2 : {data}')