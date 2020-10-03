import pylab as pl
import numpy as np
import menzalib as mz
from scipy.optimize import curve_fit


I,dI=np.array([64.42,54.03,56.14]),np.array([0.01,0.07,0.03])
t,dt=np.array([42,14,21]),np.array([1/2,1/2,1/2])

def espo(x,a,b):
	return a*np.exp(x/b)

def despo(x,a,b):
	return a/b*np.exp(x/b)

popt,pcov=curve_fit(espo,t,I,sigma=dt)

for i in range(5):
	popt,pcov=curve_fit(espo,t,I,sigma=np.sqrt(dt**2+(despo(t,*popt)*dI)**2))
x=np.linspace(13,43,100)
y=[espo(x,*popt) for x in x]
pl.errorbar(t,I,dI,dt,fmt='.')
pl.plot(x,y)
pl.ylabel('I_(th)[mA]')
pl.xlabel('T[gradi]')
pl.savefig('asd.eps',format='eps')
#pl.show()

print(popt[0],np.sqrt(pcov[0][0]))
print(popt[1],np.sqrt(pcov[1][1]))