import numpy as np

a = [1,2,3,4,5]
b = [6,7,8,9,0]

anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,0])

# Penjumlahan
jumlah = a+b
print(jumlah)
# Element wise operation
jumlah1 = anp + bnp
print(jumlah1)

# Pengurangan
kurang = anp - bnp
print(kurang)

# Perkalian
kali = anp * bnp
print(kali)

# Pembagian
bagi = anp/bnp
print(bagi)

# Kuadrat
kuadrat = anp**2
print(kuadrat)

# Multidimensi array numpy
c = np.array(([1,2,3],[4,5,6]))
d = np.array(([7,8,9],[-1,-2,-3]))

hasil1 = c + d
hasil2 = c * d

print(hasil1)
print(hasil2)