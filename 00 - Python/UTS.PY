from statistics import linear_regression
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def evalPoly(a,xData,x):
    n = len(xData) - 1 # Degree of polynomial
    p = a[n]
    for k in range(1,n+1):
        p = a[n-k] + (x -xData[n-k])*p
    return p
def coeffts(xData,yData):
    m = len(xData) # Number of data points
    a = yData.copy()
    for k in range(1,m):
        a[k:m] = (a[k:m] - a[k-1])/(xData[k:m] - xData[k-1])
    return a

xData = np.arange(0.0,6.0,0.5)
yData = np.array([1.0,0.994,0.99,0.985,0.979,0.977,0.972,0.969,0.967,0.96,0.956,0.952])
# Membuat y log natural untuk mencari nilai paruh waktu
ylnData = np.array([np.log(1.0),np.log(0.994),np.log(0.99),np.log(0.985),np.log(0.979),np.log(0.977),np.log(0.972),np.log(0.969),np.log(0.967),np.log(0.96),np.log(0.956),np.log(0.952)])

slope, intercept, r, p, std_err = stats.linregress(xData, ylnData)
# Interpolasi Newton
a = coeffts(xData,yData)
print("\nInterpolasi Newton dengan jarak 0,25 :")
print("I        t (tahun)") 
print("------------------")
for x in np.arange(0.0,5.6,0.25): 
    y = evalPoly(a,xData,x)
    print('{:3.2f} {:12.5f}'.format(x,y))

def tes(x, y):
    n = np.size(x)
    rataX = np.mean(x)
    rataY = np.mean(y)
    devY = np.sum(y*x) - n*rataY*rataX 
    devX = np.sum(x*x) - n*rataX*rataX 
    koef1 = devY / devX 
    koef2 = rataY - koef1*rataX 
    return(koef2, koef1)

koefisien = tes(xData, ylnData) 
lamda = abs(koefisien[1])
waktu_paruh = np.log(2)/lamda
print('Konstanta peluruhan =',lamda)
print("Umur Paruh Waktu =",waktu_paruh)
var1 = abs(slope)
var2 = np.log(2)/var1
print('dengan linregress konstanta peluruhan : ', var1)
print('paruh waktu dengan linregress : ', var2)

# slope dengan koefisien sama