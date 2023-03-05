import numpy as np

a = np.arange(10)**2
print(a)

# Mengambil nilai indexing
print('Elemen ke 1 dari a adalah : ', a[0])
print('Elemen akhir dari a adalah : ', a[-1])

# Slicing
print('Elemen dari 1-6 adalah : ', a[0:6])
print('Elemen ke 4 sampai akhir adalah : ', a[3:])
print('Elemen dari awal sampai ke 5 adalah : ', a[:5])

# Iterating
for i in a :
    print('Nilai = ',1)