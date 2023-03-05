import numpy as np

a = np.random.randn(1,6)
print(a)

b = np.floor(np.random.randn(1,6)*10)
print(b)

print('Maksimum dari a : ',a.max())
print('Posisi maksimum dari a : ',a.argmax())
print('Minimum dari a : ',a.min())
print('Posisi minimum dari a : ',a.argmin())

# Mengurutkan
print(np.sort(a))
print(np.argsort(a))

# Dua dimensi
print('\n' + 10*'=' + '\n')

c = np.random.randn(1,6)
print(c)

b = np.floor(np.random.randn(1,6)*10)
print(b)

print('Maksimum dari c : ',c.max())
print('Posisi maksimum dari c : ',c.argmax())
print('Minimum dari c : ',c.min())
print('Posisi minimum dari c : ',c.argmin())

# Mengurutkan
print(np.sort(c))
print(np.argsort(c))

print('\n' + 10*'=' + '\n')
dtipe = [('nama','S20'),('tinggi',int)]
data = [
    ('Amanda',187),
    ('Haiqal',188),
    ('Ipan',120)
]

d = np.array(data, dtype = dtipe)
print(d)

print(np.sort(d, order='tinggi'))
print(np.sort(d, order='nama'))