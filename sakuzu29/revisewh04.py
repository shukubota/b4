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


size1,size2=np.shape(np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata2/p1/00.dat"))
datafin=np.zeros((24,size1,size2))
countfin=datafin*0.
plotdata=np.zeros((size1,size2))
plotcount=plotdata


for i in range(1,9):
	file="p"+"%d"%i
	print file

	for j in range(0,24):

		hour="%02d"%j
		print hour
		data=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata2/"+file+"/"+hour+".dat")
		
		countdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata/"+file+"/count"+hour+".dat")
		

	
		data=data*countdata
		#print data
		datasize1,datasize2=np.shape(data)
		#print np.shape(data[:,datasize2-1])
		data=np.hstack((np.zeros((datasize1,1)),data))
		data=np.hstack((data,np.zeros((datasize1,1))))
		data=np.vstack((np.zeros((1,datasize2+2)),data))
		data=np.vstack((data,np.zeros((1,datasize2+2))))
		countdata=np.hstack((np.zeros((datasize1,1)),countdata))
		countdata=np.hstack((countdata,np.zeros((datasize1,1))))
		countdata=np.vstack((np.zeros((1,datasize2+2)),countdata))
		countdata=np.vstack((countdata,np.zeros((1,datasize2+2))))
		print np.shape(data)
		print data
		print countdata
		for m in range(1,datasize1+1):
			for n in range(1,datasize2+1):
				datafin[j,m-1,n-1]=np.sum(data[m-1:m+2,n-1:n+2])
				countfin[j,m-1,n-1]=np.sum(countdata[m-1:m+2,n-1:n+2])
		print datafin[j,:,0]
		print countfin[j,:,0]

	
	for j in range(0,24):
		hour="%02d"%j
		if j==0:
			plotdata=datafin[0,:,:]+datafin[1,:,:]+datafin[23,:,:]
			plotcount=countfin[0,:,:]+countfin[1,:,:]+countfin[23,:,:]
			print plotdata
			print plotcount
		elif j==23:
			plotdata=datafin[22,:,:]+datafin[0,:,:]+datafin[23,:,:]
			plotcount=countfin[22,:,:]+countfin[0,:,:]+countfin[23,:,:]	
		

		else:
			plotdata=np.sum(datafin[j-1:j+2,:,:],axis=0)

			plotcount=np.sum(countfin[j-1:j+2,:,:],axis=0)
		print plotdata
		print plotcount
		
		plotcount[plotcount==0.]=1.
		plotdata=plotdata/plotcount


		filename="plotdata_wh04_rv/p"+"%d"%i+"/"+"%02d"%j+".dat"
		np.savetxt(filename,plotdata,delimiter=" ")
		np.savetxt("plotdata_wh04_rv/p"+"%d"%i+"/count"+"%02d"%j+".dat",plotcount,delimiter=" ")
		


	
