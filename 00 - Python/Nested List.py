data_1 = [1,2]
data_2 = [3,4]
list_2D = [data_1,data_2]

print(f'data gabungan = {list_2D}')

# Contoh penggunaan
peserta_0 = ['amanda',20,'Laki-laki']
peserta_1 = ['haiqal',19,'laki-laki']
peserta_2 = ['manda',22,'wanita']

list_peserta = [peserta_0,peserta_1,peserta_2]

print(f'list dari peserta : {list_peserta}')

for peserta in list_peserta :
    print(f"nama\t: {peserta[0]}")
    print(f'umur\t: {peserta[1]}')
    print(f'gender\t: {peserta[2]}\n')

# Dengan reference
list_copy = list_peserta.copy();
print(f'peserta = {list_copy}')
peserta_0[0] = 'Michael'
print(f'peserta = {list_peserta}')