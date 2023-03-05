from numpy import percentile


kumpulan_angka = [1,3,2,1,3]
for angka in kumpulan_angka:
    print(f'angka : {angka}')


peserta = ['a','v','c']
for nama in peserta:
    print(f'nama : {nama}')

kumpulan_angka = [1,3,2,1,3]
panjang = len(kumpulan_angka)
i = 0
while i < panjang:
    print(i)
    i += 1

# List compreherension
data = [1,2,3,'w','w']
[print(f'data : {data}') for i in data]

angka = [2,4,5,6]
kuadrat = [i**2 for i in angka]
print(kuadrat)

# Enumerate
data_list = [1,2,3,2,1]

for i, data in enumerate(data_list):
    print(f'i = {i}, data = {data}')