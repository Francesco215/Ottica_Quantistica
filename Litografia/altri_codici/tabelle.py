import menzalib as mz
import numpy as np


num_tacchette=np.array([45,18,10,5])
micron=num_tacchette*100
Lmax,Lmin=np.array([2005,1935,1994,1863]),np.array([1990,1892,1907,1753])
L,dL=(Lmax+Lmin)/2,(Lmax-Lmin)/2
mpp,dmpp=np.empty(len(micron)),np.empty(len(micron))#micron per pixel
for i in range(len(L)): 
    mpp[i]=micron[i]/L[i]
    dmpp[i]=mz.drapp(1,0,L[i],dL[i])


zoom=np.array([[0,0,1,1,3,3],
               [1,1,2,2,3,3],
               [1,1,2,2,3,3]])
Lmax=np.array([[638,767,803,1894,540,921],
               [1162,1224,519,423,201,193],
               [678,685,1040,1041,670,677]])
Lmin=np.array([[613,747,772,1865,507,863],
               [1146,1205,484,394,156,155],
               [654,669,1027,1023,644,631]])

def tabella(zoom,Lmax,Lmin):
    ingrandimento=['4x','10x','20x','40x']
    orientamento=[', verticale',', orizzontale']
    L,dL=(Lmax+Lmin)/2,(Lmax-Lmin)/2
    lung,dlung=np.empty(len(zoom)),np.empty(len(zoom))
    col1=[]
    for i in range(len(zoom)):
        lung[i]=L[i]*mpp[zoom[i]]
        dlung=mz.dprod(L[i],dL[i],mpp[zoom[i]],dmpp[zoom[i]])
        col1.append(ingrandimento[zoom[i]]+orientamento[zoom[i]%2])
    #Linea di codice di prima (sbagliata)
    #M=[col1,mz.ns_tex(Lmax),mz.ns_tex(Lmax),mz.ne_tex(L,dL),mz.ne_tex(lung,dlung)]
    M=[col1,mz.ns_tex(Lmax),mz.ns_tex(Lmin),mz.ne_tex(L,dL),mz.ne_tex(lung,dlung)]
    mz.mat_tex(M)
    
tabella(zoom[2],Lmax[2],Lmin[2])