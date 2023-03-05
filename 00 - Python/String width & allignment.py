# Data
data_nama = "Amanda Haiqal"
data_umur = 20
data_tinggi = 180.2
data_nomor_sepatu = 42

# String standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, no sepatu = {data_nomor_sepatu}"
print(6*"="+"Data Standard"+6*"=")
print(data_string)

# String Multiline (dengan menggunakan enter, newline, \n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nno sepatu = {data_nomor_sepatu}"
print("\n"+6*"="+"Data Multiline"+6*"=")
print(data_string)

# String multiline (dengan menggunakan kutip triplets)
data_string = f"""Nama = {data_nama}
Umur = {data_umur}
Tinggi = {data_tinggi}
No Sepatu = {data_nomor_sepatu}
"""
print("\n"+6*"="+"Data Multiline"+6*"=")
print(data_string)

data_string = f"""Nama = {data_nama}
Umur = {data_umur:>6}
Tinggi = {data_tinggi:>6}
No Sepatu = {data_nomor_sepatu:>6}
"""
print("\n"+6*"="+"Data Multiline"+6*"=")
print(data_string)