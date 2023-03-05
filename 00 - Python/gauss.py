import numpy as np                                        # Import Numpy sebagai Library

# Matriks yang akan digunakan diperhitungan :
a = np.array([
              [3, -0.1, -0.2],
              [0.1, 7, -0.3],
              [0.3, -0.2, 10]],
              float)
b = np.array([
              [7.85],
              [-19.0],
              [71.4]],
              float)

def GaussJordan(a,b):                                     # Membuat Fungsinya
    n = len(b)                                            # Penetapan
    
    for k in range(0,n-1):                                # k = diagonal
        for i in range(k+1,n):                            # i = baris
            a[i,k] != 0.0                                 #jika a(i,j) tidak = 0 maka diskip, jika tdk maka lanjut ke pehitungan
            lam = a[i,k]/a[k,k]                          #koefisien lambda = a_ik / a_kk
            a[i,k:n] = a[i,k:n]-lam*a[k,k:n]             #nilai elemen a baru
            b[i] = b[i]-lam*b[k]                         # Baris matriks b = baris matriks b dikurangi lambda dikali kolom matriks b
          
    for i in reversed(range(0,n-1)):                      # Untuk i didalam range matriks yang dibalik
        for k in reversed(range(i+1,n)):                  # Untuk k didalam range matriks yang dibalik
            if a[i,k] != 0:                               # Jika matriks a tidak sama dengan 0, maka:
                lam = a[i,k] / a[k,k]                     # Lambda = baris dan kolom matriks a dibagi dengan kolom matriks a
                a[i,k:n] = a[i,k:n] - lam*a[k,k:n]        # matriks a = matriks a lama dikurang lambda dikali kolom matriks a
                b[i] = b[i] - lam*b[k]                    # baris matriks b = baris matriks b yang lama dikurangi lambda dikali kolom
    
    for i in range(0,n):                                  # Untuk i didalam range baris 0,n
        for k in range(0,n):                              # Untuk j didalam range kolom 0,n
            if(a[i,i] != 1):                              # Jika baris matriks a tidak sama dengan 1, maka:
                b[i] /= a[i,i]                            # Baris matriks b dibagi dengan baris matriks a
                a[i,i] /= a[i,i]                          # Baris matriks a dibagi dengan baris matriks a
    return b                                              # Mengembalikan nilai ke b
                
print(f'Matriks A: \n {a}')
print(f'Matriks B: \n {b}')
np.set_printoptions(precision=3)
GaussJordan(a,b)
print(f'Hasilnya : \n {b}')
x=a[:,1]
print(x)