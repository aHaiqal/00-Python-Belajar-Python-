'''Fungsi dengan argument (input)'''

# def nama_fungsi(input/argument/parameter):

def hello_world(nama):
    '''Fungsi Hello world meneriman input'''
    print(f'selamat datang {nama}')
    
hello_world("Haiqal")

# program tambah

def tambah(angka_1, angka_2):
    hasil = angka_1 + angka_2
    print(f'{angka_1} + {angka_2} = {hasil}')
tambah(2,3)
tambah(121211,222)

def say_hi(list_peserta):
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f'Halo {peserta}')

anggota = {'A','B','C'}
say_hi(anggota)