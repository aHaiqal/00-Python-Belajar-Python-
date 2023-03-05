# Date and Time

import datetime as dt

hari_ini = dt.date.today()
print(hari_ini)

hari_ini = dt.date.today()
print(f"Hari ini adalah = {hari_ini:%A}")

tanggal = dt.date(2001,11,4)
print(F"Hari waktu itu = {tanggal:%A}")

print('Masukan tanggal, bulan , tahun lahir anda !')
Tanggal =  int(input('Tanggal \t: '))
Bulan = int(input('Bulan \t\t: '))
Tahun = int(input('Tahun \t\t: '))

tanggal_lahir = dt.date(Tahun,Bulan,Tanggal)
print(f"Tanggal lahir anda adalah = {tanggal_lahir}")
print(f'Hari nya adalah = {tanggal_lahir:%A}')

hari_ini = dt.date.today()
print(f'Hari ini tanggal = {hari_ini}')
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days % 365) // 30
print(f"Umur anda adalah = {umur_tahun} tahun, {umur_bulan} bulan")

