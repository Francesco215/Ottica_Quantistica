import numpy
import pylab as plt
from scipy.optimize import curve_fit
import menzalib as mz

I,P,dP=plt.loadtxt('1_T42.txt',unpack=True)

dI=0.1
plt.figure(1)

plt.grid()


fpp=numpy.array([I[0], I[1], I[2], I[3], I[4], I[5], I[6]])
dfpp=dI
pp=numpy.array([P[0], P[1], P[2], P[3], P[4], P[5], P[6]])
dpp=numpy.array([dP[0], dP[1], dP[2], dP[3], dP[4], dP[5], dP[6]])

t1=numpy.linspace(63, 80, 10000)


def rettapp(t1,n,q):
    #  return numpy.log10(tass(t,m,q))
    return q+n*t1

poptpp, pcovpp= curve_fit(rettapp, fpp, pp, ( 20., 0), dpp)

plt.plot(t1, rettapp(t1, *poptpp), linestyle='-', color='grey')


plt.ylim((9,5000))
plt.xlim((24,80))



plt.xlabel("Intensita' di corrente [mA]")
plt.ylabel("Potenza [$\mu$W]")
plt.grid(color = "grey")
plt.errorbar(I, P, dP, dI, fmt="o", markersize=1, capsize=2, color="red", label="T=42")
plt.legend()





I,P,dP=plt.loadtxt('1_T21.txt',unpack=True)
dI=0.1

plt.grid()


fss=numpy.array([I[0], I[1], I[2], I[3], I[4], I[5], I[6], I[7], I[8], I[9], I[10], I[11]])
dfss=dI
ss=numpy.array([P[0], P[1], P[2], P[3], P[4], P[5], P[6], P[7], P[8], P[9], P[10], P[11]])
dss=numpy.array([dP[0], dP[1], dP[2], dP[3], dP[4], dP[5], dP[6], dP[7], dP[8], dP[9], dP[10], dP[11]])

t2=numpy.linspace(55, 80, 10000)


def rettass(t2,m,r):
    #  return numpy.log10(tass(t,m,q))
    return r+m*t2

poptss, pcovss= curve_fit(rettass, fss, ss, ( 20., 0), dss)

plt.plot(t2, rettass(t2, *poptss), linestyle='-', color='grey')


plt.errorbar(I, P, dP, dI, fmt="o",markersize=1, capsize =2, color="green", label="T=21"  )
plt.legend()





I,dI, P,dP=plt.loadtxt('1_T14.txt',unpack=True)


plt.grid()


frr=numpy.array([I[0], I[1], I[2], I[3], I[4], I[5], I[6], I[7], I[8]])
dfrr=dI
rr=numpy.array([P[0], P[1], P[2], P[3], P[4], P[5], P[6], P[7], P[8]])
drr=numpy.array([dP[0], dP[1], dP[2], dP[3], dP[4], dP[5], dP[6], dP[7], dP[8]])

t3=numpy.linspace(50, 80, 10000)


def rettarr(t3,l,w):
    #  return numpy.log10(tass(t,m,q))
    return w+l*t3

poptrr, pcovrr= curve_fit(rettarr, frr, rr, ( 20., 0), drr)

plt.plot(t3, rettarr(t3, *poptrr), linestyle='-', color='grey')



plt.errorbar(I, P, dP, dI, fmt="o",markersize=1,  capsize =2, color="blue", label="T=14" )
plt.legend()


"""print("T42:")
print('mC= %f +- %f' %(poptpp[0],numpy.sqrt(pcovpp[0,0])))
print('qC= %f +- %f' %(poptpp[1],numpy.sqrt(pcovpp[1,1])))
print('corr_pp= %f' % (pcovpp[0,1]/numpy.sqrt(pcovpp[0,0]*pcovpp[1,1])))
print('\n')
print("T21:")
print('mC= %f +- %f' %(poptss[0],numpy.sqrt(pcovss[0,0])))
print('qC= %f +- %f' %(poptss[1],numpy.sqrt(pcovss[1,1])))
print('corr_pp= %f' % (pcovss[0,1]/numpy.sqrt(pcovss[0,0]*pcovss[1,1])))
print('\n')
print("T14:")
print('mC= %f +- %f' %(poptrr[0],numpy.sqrt(pcovrr[0,0])))
print('qC= %f +- %f' %(poptrr[1],numpy.sqrt(pcovrr[1,1])))
print('corr_pp= %f' % (pcovrr[0,1]/numpy.sqrt(pcovrr[0,0]*pcovrr[1,1])))
print('\n')
plt.savefig("curvacaratt.png")
plt.show()"""


def f(popt):
	return -popt[1]/popt[0]

def gradf(popt):
	return [popt[1]/popt[0]**2,-1/popt[0]]



print(mz.ne_tex(f(poptpp),mz.dy(f,poptpp,pcovpp,gradf),"A"))
print(mz.ne_tex(f(poptrr),mz.dy(f,poptrr,pcovrr,gradf),"A"))
print(mz.ne_tex(f(poptss),mz.dy(f,poptss,pcovss,gradf),"A"))





