# Operasi Komparasi

# Setiap hasil dari operasi komparasi adalah boolean

# >, < ,>=, <=, ==, !=, is not

a = 4
b = 2

# Lebih besar dari >
print('====LEBIH BESAR DARI===')
hasil = a > 3
print(a,'>',3,'=', hasil)

hasil = b > 2
print(b,'>',2,'=',hasil)

# Lebih kecil dari <
print('====KURANG DARI====')
hasil = a < 3
print(a,'<',3,'=',hasil)

hasil = b < 3
print(b,'<',3,'=',hasil)

# Lebih dari sama dengan
print('====LEBIH BESAR SAMA DENGAN===')
hasil = a >= 3
print(a,'>=',3,'=', hasil)

hasil = b >= 3
print(b,'>=',3,'=',hasil)

# Lebih kecil sama dengan
print('====LEBIH KECIL SAMA DENGAN====')
hasil = a <= 3
print(a,'<=',3,'=', hasil)

hasil = b <= 3
print(b,'<=',3,'=',hasil)

# Sama dengan ==
print('====SAMA DENGAN====')
hasil = a == 4
print(a,'==',4,'=',hasil)

hasil = b == 4
print(b,'==',4,'=',hasil)

# Tidak sama dengan !=
print('====TIDAK SAMA DENGAN====')
hasil = a != 4
print(a,'!=',4,'=',hasil)

hasil = b != 4
print(b,'!=',4,'=',hasil)

# Is sebagai komparasi objek
print('====Object Identity====')
x = 5 # ini adalah assigment membuat objek
y = 5
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)

x = 5 # ini adalah assigment membuat objek
y = 6
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is y =',hasil)