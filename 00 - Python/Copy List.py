# Teknik menduplikat list

from re import A


a = ["Ipan","Paissl"]
print(f'a = {a}')

b = a # Pass by reference
print(f'b = {b}')

# Copy list dengan copy
c = a.copy() # Full duplikat
print(f'c = {c}')
print(f'adress dari a = {hex(id(a))}')
print(f'adress dari b = {hex(id(b))}')
print(f'adress dari c = {hex(id(c))}')

print(f'\n'+'ubah data c'+'\n')
c[0] = 'Lipan'
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')