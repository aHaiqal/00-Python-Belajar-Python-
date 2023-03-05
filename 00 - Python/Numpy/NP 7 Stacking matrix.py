import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

# Stacking matrix / menumpuk matrik

c = np.hstack((a,b))
d = np.vstack((a,b))
print(c)
print(d)

aMat = np.zeros((2,2))
bMat = np.ones((2,2))

cMat = np.hstack((aMat,bMat))
dMat = np.vstack((aMat,bMat))
print(cMat)
print(dMat)