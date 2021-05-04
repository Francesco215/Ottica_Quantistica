import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


def lin_interp(x, y, i, half):
    return x[i] + (x[i+1] - x[i]) * ((half - y[i]) / (y[i+1] - y[i]))

#finds the value of y for witch y=f(x) in couple of array x=[x_1,x_2,...,x_n] and y=[y_1,y_2,...,y_n]
def intersection(x,y,const):
    signs = np.sign(np.add(x, -const))
    zero_crossings = (signs[0:-2] != signs[1:-1])
    zero_crossings_i = np.where(zero_crossings)[0]
    return [lin_interp(y, x, zero_crossing,const) for zero_crossing in zero_crossings_i]


data = pd.read_csv('potenza_angolo.txt', sep="\t")
data=data.sort_values(by=['Angolo'])
ang,W=np.transpose(data.values)
NA=intersection(W,ang,np.amax(W)/20)

plt.plot(NA,np.amax(W)/20*np.array([1,1]))
plt.plot(ang,W)
plt.ylabel('Potenza[μW]')
plt.xlabel('Angolo[deg]')
#plt.savefig('potenza_angolo.eps',format='eps')
#plt.savefig('potenza_angolo.png')
print((NA[1]-NA[0])/2)