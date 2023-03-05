#Dictionary
data_list = ['ayam','bebek','cicak']

data_dict = {
    'key1' : 'value1',
    'aym' : 'ayam',
    'bbk' : 'bebek',
    'cck' : 'cicak',
    'no' : 100,
    'list' : data_list
}

print(data_dict['aym'])
print(data_dict['list'])
print(data_dict['no'])

# Panjang dictionary
LENDICT = len(data_dict)
print(f'Panjang dictionary : {LENDICT}')

# Mengecek key exist atau tidak
KEY = 'cck'
CHECKKEY = KEY in data_dict
print(f'Apakah {KEY} ada di data dict : {CHECKKEY}')

# Mengakses value (read) dengan get
print(data_dict.get('cck'))
print(data_dict.get(100, "Key tidak ada"))

# Mengupdate data
data_dict['cck'] = 'Cicicak'
print(data_dict)

data_dict.update({'cck':'caick'})
print(data_dict)

# Menghapus data
del data_dict['cck'] 
print(data_dict)

# Looping dictionary :
teman_teman = {
    "cup":"ucup cup",
    "tong":"gentong",
    "dung":"dudung",
}
# Looping first try (yg keluar adalah key nya)
for teman in teman_teman:
    print(teman)

# operator utnyuk mengambil item / iterables
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key))

values = teman_teman.values()
print(values)
for value in teman_teman.values():
    print(value)

items = teman_teman.items()
print(items)
for item in teman_teman.items():
    print(item)

for key, value in teman_teman.items():
    print(f"key = {key}, value = {value}")