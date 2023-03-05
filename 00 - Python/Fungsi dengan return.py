from sympy import re


def kuadrat(x):
    hasil = x**2
    return hasil

y = kuadrat(9)
print(y)

def vol_persegi(sisi):
    return sisi*sisi
y = vol_persegi(3)
print(y)

def operasi(angka1, angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2
    return tambah, kurang, kali, bagi

k,l,m,n = operasi(9,8)
print(f'Hasil tambah = {k}')
print(f'Hasil kurang = {l}')
print(f'Hasil kali = {m}')
print(f'Hasil bagi = {n}')