# Kumpulan data numbers
data_angka = [1,2,3]
print(data_angka)

# Kumppulan data string
data_string = ['haiqal','amanda']
print(data_string)

# Kumpulan data boolean
data_boolean = [True,False,True,False]
print(data_boolean)

# Kumpulan campuran
data_campuran = [1,'bala-bala',2,'peang',True]
print(data_campuran)

# Cara alternatif
data_range = range(0,10,2) #start, stop, step
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for
data_list_for = [i**2 for i in range(0,10)]
print(data_list_for)

# membuat list dgn for if
list_for_if = [i for i in range(0,10) if i % 2 == 0]
print(list_for_if)

list_for_if = [i for i in range(0,10) if i % 2 != 0]
print(list_for_if)

list_for_if = [i for i in range(0,10) if i != 5]
print(list_for_if)

list_for_if = [i**2 for i in range(0,10) if i % 2 != 0]
print(list_for_if)