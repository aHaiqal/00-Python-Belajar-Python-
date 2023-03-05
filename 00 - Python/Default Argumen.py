'''Default Arguments'''

# def fungsi argument
# def fungsi(argumen = nilai defaultnya)

def haloo(nama = "Ganteng"):
    '''fungsi dengan argumen'''
    print(f"Halo {nama}")
    
haloo("Ipan")
haloo()

def sapa_dia(pesan,nama):
    '''fungsi dengan satu input biasa dan satu default argumen'''
    print(f"hai {nama}, {pesan}")
    
sapa_dia("Woi", "ipan")

def hitung(angka, pangkat):
    return angka**pangkat

print(hitung(2,4))
hasil = hitung(pangkat=2, angka=5) # untuk mengubah 
print(hasil)

hasil1 = hitung(pangkat=3) # untuk mengubah 
print(hasil1)