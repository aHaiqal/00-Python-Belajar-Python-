# Perkalian vektor (Aljabar  Linier)

from gettext import npgettext
import numpy


import numpy as np


# Perkalian dot
## 2 Dimensi
a = np.array([1,3])
b = np.array([3,0])

c = np.dot(a,b)
print(c)

## 3 Dimensi
d = np.array([1,3,2])
e = np.array([3,0,4])

f = np.dot(d,e)
print(f)

# Perkalian cross
g = np.array([1,2,0])
h = np.array([2,1,0])

i = np.cross(g,h)
print(i)