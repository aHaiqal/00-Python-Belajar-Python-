import numpy as np

#fase dekomposisi (eliminasi)
def dekomposisiLU(a):
    n = len(matA)
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lamb = a[i,k]/a[k,k]
                a[i,k:n] = a[i,k:n] - lamb*a[k,k:n]
                a[i,k] = lamb
    return a

#fase solusi (substitusi maju)
def solusiLU(matA,matB):
    n = len(matA)
    for k in range(1,n):
        matW[k] = matW[k] - np.dot(matA[k,0:k],matW[0:k])
    matW[n-1] = matW[n-1]/matA[n-1,n-1]
#masuk ke solusi Gauss
    for k in range(n-2,-1,-1):
        matW[k] = (matW[k]-np.dot(matA[k,k+1:n],matW[k+1:n]))/matA[k,k]
    return matW

matA = np.array([[3, -1,-1, 0, 0, 0],
                 [-1, 4, -1, -1, 0, 0],
                 [-1, -1, 4, -1, -1, 0],
                [0, -1, -1, 4, -1, -1],
                [0, 0, -1, -1, 4, -1],
                [0, 0, 0, -1, -1, 3]],float)
matW = np.array([[1],
                 [1],
                 [1],
                 [0],
                 [0],
                 [0],
                 [0]],float)

print(f'Matriks A : {matA}\nVektor V : {matW}')

solusiLU(matA,matW)
print('hasil = \n', matW)







