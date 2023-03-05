import imp


import numpy as np

a = np.array((
              [1,2,3],
              [4,5,6]
))
print('Matrix a dengan ukuran', a.shape)
print(a)

# Transpose matrix
print('Transpose matriks dari a :')
print(a.transpose())
print(np.transpose(a))
print(a.T)
print('Matrix a dengan ukuran : ',a.shape)

# Flatten array / vector baris
print('Flatten matrix a:')
print(a.ravel())
print(np.ravel(a))
print('Matrix a dengan ukuran : ',a.shape)

# Reshape matrix
print('reshape matrix a :')
print(a.reshape(3,2))
print(a.reshape(6,1))
print('Matrix a dengan ukuran : ',a.shape)

# Resize matrix
print('Resize matrix a:')
a.resize(3,2)
print(a)
print('Matrix a dengan ukuran : ',a.shape)

