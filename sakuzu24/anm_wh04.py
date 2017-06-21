#coding:utf-8

import numpy as np

plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu24/plotdata_wh04/dailyp01.dat",delimiter=",")


m,n=np.shape(plotdata)

plotdata=np.zeros((m,n))
countdatasum=np.zeros((m,n))
for phase in range(1,9):
	plotcp=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu24/plotdata_wh04/dailyp"+"%02d"%phase+".dat",delimiter=",")
	countdata=np.load("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu24/plotdata_wh04/count24h%02d.npy"%phase)
	plotdata+=plotcp*countdata
	countdatasum+=countdata
	np.save("plotdata_wh04/countfor8p%02d.npy"%phase,countdatasum)

countdatasum[countdatasum==0]=1
plotdata=plotdata/countdatasum


for phase in range(1,9):
	plotcp=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu24/plotdata_wh04/dailyp"+"%02d"%phase+".dat",delimiter=",")
	plotcp-=plotdata

	file="/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu24/plotdata_wh04/anmdaily"+"%02d"%phase+".dat"
	np.savetxt(file,plotcp,delimiter=",")