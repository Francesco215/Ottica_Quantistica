import menzalib as mz
import numpy as np

def f(popt):
	return popt[0]/popt[1]

print(f(popt),mz.dy(f,popt,pcov))