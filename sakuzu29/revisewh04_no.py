#coding:utf-8

import numpy as np


#########################
lon1=70.
lon2=160.
lat1=-15.
lat2=30.
grid=0.1
resnum=3 #odd number onlyi

lag=int(resnum/2)
##############################





for i in range(1,9):
	file="p"+"%d"%i
	print file

	for j in range(0,24):

		hour="%02d"%j
		print hour
		data=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_no/"+file+"/"+hour+".dat")

		mmax,nmax=np.shape(data)
		datarv=data
		print np.shape(datarv)

		mend=mmax-(int(resnum/2)+1)
		nend=nmax-(int(resnum/2)+1)
		#print mmax,nmax
		mstart=int(resnum/2)
		nstart=int(resnum/2)
		print "mstart,mend,nstart,nend",mstart,mend,nstart,nend 
		#print np.shape(data)



		#test=([1,2,3,4],[2,3,4,5])
		#print test
		#ave=np.average(test[0])
		#print ave
		#print np.shape(test)
		for k in range(mstart,mend+1):
			for l in range(nstart,nend+1):	
				datarv[k,l]=np.average(data[k-lag:k+lag+1,l-lag:l+lag+1])


		#print datarv

		filename="plotdata_no/p"+"%d"%i+"/"+"%02d"%j+".dat"
		np.savetxt(filename,datarv,delimiter=" ")
	
