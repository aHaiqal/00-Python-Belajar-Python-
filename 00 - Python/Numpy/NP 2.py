import numpy as np

# Membuat vektor
print(10*'=')
a = np.array([1,2,3,4,5])
b = np.array([1.5 , 2.5 , 3.5 , 6 , 7])
print(b)

# Membuat vektor dengan range
print(10*'=')
c = np.arange(1,10,2)
print(c)

# Membuat linear space
print(10*'=')
d = np.linspace(1,10,4)
print(d)

# Membuat array multidimensi / matriks
print(10*'=')
e = np.array( [ (1,2,3) , (4,5,6)] )
print(e)

# Matrix dengan nilai nol
print(10*'=')
f = np.zeros((5,5))
print(f)

# Matrix dengan nilai satu
print(10*'=')
g = np.ones((5,5))
print(g)

# Matrix identitas
print(10*'=')
h1 = np.identity(3)
h2 = np.eye(3)
print(h1)
print(h2)