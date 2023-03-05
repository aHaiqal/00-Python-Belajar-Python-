import numpy as np

a = np.array(([1,2],
                [3,4]))

b = np.ones([2,2])

print(a)
print(b)

# Perkalian matriks
c1 = np.dot(a,b)
print(c1)

c2 = a.dot(b)
print(c2)

d = np.array(([1,2,5],[3,4,6]))
f = np.ones([3,1])
e = np.dot(d,f)
print(e)