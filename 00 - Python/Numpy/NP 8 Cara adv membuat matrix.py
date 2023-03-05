import numpy as np

# Membuat matrix dengan tipe data tertentu
a = np.array(([1,2,3],[4,5,6]), dtype= float)
print(a)

b = np.array(([1,2,3],[4,5,6]), dtype= bool)
print(b)

# Membuat matrix dengan fungsi
def kuadrat(baris,kolom):
    return kolom**2

c = np.fromfunction(kuadrat,(1,10), dtype = int) # fungsi, ukuran matriks, tipe
print(c)

def jumlah(baris,kolom):
    return [kolom + baris]

d = np.fromfunction(jumlah,(4,4), dtype = float) # fungsi, ukuran matriks, tipe
print(d)

# Membuat matrix dengan iterable

iterable = (x*2 for x in range(5))
e = np.fromiter(iterable, dtype=int)
print(e)

# Membuat multitype array
data = [
    ('ucup', 177),
    ('otong', 167),
    ('mario', 180)
]
print(data)