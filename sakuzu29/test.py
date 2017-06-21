#coding:utf-8
#mjo phase grid 修正版
import numpy as np
import os 
from pyhdf.SD import SD, SDC
import time
import glob
import gc

if __name__ == '__main__':
	start = time.time()

hdf=SD("data/2A25.19980112.00711.7.HDF",SDC.READ)
data3D=hdf.select('rainType')
data=data3D[:]
np.savetxt("test.dat",data)
print data
