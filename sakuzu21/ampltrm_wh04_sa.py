#coding:utf-8

import numpy as np
import time

if __name__ == '__main__':
    start = time.time()




m,n=np.shape(np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu36/plotdata_wh04_rv/00.dat"))
##################
#size of plotdata(m,n)
##################
#m=451
#n=901
########################
#hour step
hourstep=1


#file=open("./sakuzu20/plotdata/p1/


phase=0
data=np.zeros((24,m,n))
pi=np.arctan(1.)*4.
#print pi

for i in range(1,2):
    file="p"+"%d"%i
    
    A=np.zeros((m,n))
    B=np.zeros((m,n))
    C=np.zeros((m,n))
    phi=np.zeros((m,n))
    #data=np.zeros((24,
    for j in range(0,24):
        hour="%02d"%j
	rep=j/hourstep
        data[j]=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu36/plotdata_wh04_rv/"+hour+".dat")
        #print np.shape(data)
        A+=data[j]*np.cos(2.*pi*rep*hourstep/24.)
        B+=data[j]*np.sin(2.*pi*rep*hourstep/24.)

    A=A/24.
    B=B/24.
    C=np.sqrt(A*A+B*B)
    condition=np.where((A>0.) & (B>=0.))
    phi[condition]=np.arctan(B[condition]/A[condition])
    condition=np.where((A>0.) & (B<0.))
    phi[condition]=np.arctan(B[condition]/A[condition])+2.*pi
    condition=np.where((A<0.) & (B>=0.))
    phi[condition]=np.arctan(B[condition]/A[condition])+pi
    condition=np.where((A<0.) & (B<0.))
    phi[condition]=np.arctan(B[condition]/A[condition])+pi
    condition=np.where((A==0.) & (B==0.))
    phi[condition]=0.
    condition=np.where((A==0.) & (B>0.))
    phi[condition]=pi*0.5
    condition=np.where((A==0.) & (B<0.))
    phi[condition]=pi*1.5
    #print data[0]

    phi=phi*24/(2.*pi)

    filephi="plotdata_wh04/sa/phi.dat"
    filec="plotdata_wh04/sa/c.dat"
    np.savetxt(filephi,phi,delimiter=",")
    np.savetxt(filec,C,delimiter=",")


elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
