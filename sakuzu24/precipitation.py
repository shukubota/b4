#coding:utf-8
import numpy as np
import time


if __name__ == '__main__':
	start = time.time()

##################
#size of plotdata(m,n)
##################
m=451
n=901
########################



for j in range(1,9):
	plotdata=np.zeros((m,n))
	file="p"+"%d"%j
	for i in range(0,24):
		hour="%02d"%i
		
		#data=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_1209/"+file+"/"+hour+".dat")
		data=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_bimodal_rv/"+file+"/"+hour+".dat")
		plotdata+=data

	plotdata=plotdata/24.

	filename="plotdata/dailyp"+"%02d"%j+".dat"
	#file=open(filename,"w")
 	np.savetxt(filename,plotdata,delimiter=",")
	

elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"
