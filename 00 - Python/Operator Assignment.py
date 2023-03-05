# Operasi yang dapat dilakukan dengan penyingkatan
# Operasi ditambah dengan assignment

a = 5 # adalah assignment
print('Nilai dari a :',a)

a += 1 # artinya adalah a = a + 1 
print("Nilai dari a += 1 :, nilai menjadi",a)

a -= 2 # artinya adalah a = a - 2
print("Nilai dari a -= 2 :, nilai menjadi",a)

a *= 5 # artinya adalah a = a * 5
print("Nilai dari a *= 5:, nilai menjadi",a)

a /= 2 # artinya adalah a = a / 2
print("Nilai dari a /= 2:, nilai menjadi",a)

# Modulus dan floor division
b = 10
print("\nNilai dari b :",b)

b %= 3
print("Nilai dari b %= 3, nilai b menjadi",b)

b //= 3
print("Nilai dari b //= 3:, nilai menjadi",b)

a = 5 
print('Nilai dari a :',a)
a **= 3
print("Nilai dari a **= 3:, nilai menjadi",a)

# Operasi bitwise
#OR
c = True
print("\nNilai c =",c)
c |= False
print("Nilai c |= False, nilai c menjadi :",c)
c = False
print("Nilai c =",c)
c |= False
print("Nilai c |= False, nilai c menjadi :",c)

# AND 
c = True
print("\nNilai c =",c)
c &= False
print("Nilai c &= False, nilai c menjadi :",c)
c = True
print("Nilai c =",c)
c &= True
print("Nilai c &= True, nilai c menjadi :",c)

# XOR
c = True
print("\nNilai c =",c)
c ^= False
print("Nilai c ^= False, nilai c menjadi :",c)
c = True
print("Nilai c =",c)
c ^= True
print("Nilai c ^= True, nilai c menjadi :",c)

# Geser geser
d = 0b0100
print("Nilai d =",format(d,'04b'))
d >>= 2
print("Nilai d >>= 2, nilai d menjadi",format(d,'04b'))
d <<= 1
print("Nilai d << = 1, nilai d menjadi",format(d,'04b'))