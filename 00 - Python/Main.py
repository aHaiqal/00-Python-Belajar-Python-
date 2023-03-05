# variabel adLh tempat menyimpan data

# assignment nilai
# a = 10, a adalah vaariabel dengan nilai 10
a= 10
x = 5
panjang = 1000

#pemanggilan pertama
print("Nilai a = ", a)
print("Nilai x = ", x)
print("Nilai panjang = ", panjang)

# penamaan
nilai_y = 15 # dengan menggunakan underscore 
juta10 = 10000000 # ini boleh
nilaiZ = 16 # ini boleh

#pemanggilan kedua
print("Nilai a = ", a)
a = 7
print("Nilai a =", a)

#assisgment indirect
b = a
print("Nilai b =", b)




# tipe data: angka satuan (integer)
data_integer = 1
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

#tipe data: float (angka dengan koma)
data_float = 1,5
print("data : ", data_float)
print("- bertipe : ", type(data_float))

# tipe data: kumpulan karakter (string)
data_string = "haiqal 10"
print("data : ", data_string)
print("- bertipe : ", type(data_string))

# tipe data: biner true/false (boolean)
data_bool = True
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))

# tipe data khusus
## bilangan kompleks
data_complex = complex(4,5)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

# tipe data dari bahasa C

from ctypes import c_double, c_char

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))