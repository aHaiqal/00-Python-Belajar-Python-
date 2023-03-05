# Contoh umum
# String
nama = "Haiqal"
format_str = f"Halo {nama}"
print(format_str)

# Angka
angka = 2001.1
format_str = f"Angka = {angka}"
print(format_str)

# Boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# Bilangan bulat
angka = 23
format_str = f"angka = {angka:d}"
print(format_str)

# Bilangan ribuan
angka = 2000000
format_str = f"angka = {angka:,}"
print(format_str)

# Bilangan desimal
angka = 2001.1234
format_str = f"Desimal = {angka:.3f}"
print(format_str)

# Menampilkan leading zero
angka = 2001.1234
format_str = f"Desimal = {angka:012.3f}"
print(format_str)

# Menampilkan tanda + -
angka_plus = +4
angka_minus = -4
format_plus = f"plus = {angka_plus:+d}"
format_minus = f"minus = {angka_minus:+d}"

print(format_plus)
print(format_minus)

angka_plus = +4
angka_minus = -4
format_plus = f"plus = {angka_plus:+.4f}"
format_minus = f"minus = {angka_minus:+.2f}"

print(format_plus)
print(format_minus)

# Memformat persen
persentase = 0.0098
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# Melakukan operasi aritmatika di dalam placeholder {}
Harga = 20000
Jumlah = 6
format_str = f"total harga = Rp. {Harga*Jumlah:,}"
print(format_str)

# Format angka lain (binary, octal, hex)
angka = 2301
binary = f"binary = {bin(angka)}"
octal = f"octal = {oct(angka)}"
hex = f"hex = {hex(angka)}"
print(binary)
print(octal)
print(hex)