list_buku = []

while True :
    print('\n','Masukkan data buku : ')
    judul = input('Judul Buku   : ')
    penulis = input('Nama Penulis : ')

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)

    print('\n',10*'=','Data Buku',10*'=')
    for index,buku in enumerate(list_buku):
        print(f'{index+1} | {buku[0]} | {buku[1]}')

    print('\n','='*10)
    isLanjut = input('Apakah lanjut ? (y/n) ')


    if isLanjut == 'n':
        break

print('Selesai')
