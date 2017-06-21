#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt


lon1=70.
lat1=-15
grid=0.1

########
#調べたい場所
#######
lon=114.
lat=2.


m=int((lon-lon1)/grid)
n=int((lat-lat1)/grid)



#m=260
#n=300
#m=500
#n=300
#m=900
#n=450
#m=
#n=

a=0.
b=0.
c=0.
mean=0.
sum2=0.
pi=np.arctan(1.)*4.


plot=np.zeros(24)
for j in range(0,24):
	hour="%02d"%j
	data=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu29/plotdata_wh04_rv/p2/"+hour+".dat")
	plot[j]=data[n,m]

	#if j==0:
	#	plot[j]=plot[j]+plot[j+1]+plot[23]
	#	plot[j]=plot[j]/3.
	
	#elif j==23:
	#	plot[j]=plot[j]+plot[j-1]+plot[0]
	#	plot[j]=plot[j]/3.

	#else:
	#	plot[j]=plot[j]+plot[j+1]+plot[j-1]
	#	plot[j]=plot[j]/3.

for j in range(0,24):


	mean+=plot[j]
	a+=plot[j]*np.cos(2.*pi*(j+0.5)/24)
	b+=plot[j]*np.sin(2.*pi*(j+0.5)/24)
	sum2+=plot[j]*plot[j]
a=a/12.
b=b/12.
mean=mean/24.

s2=(sum2-24.*mean*mean-0.5*24.*(a*a+b*b))/(24.-3.)
f=24.*(a*a+b*b)/(4.*s2)
print "f",f

print plot



	



x=np.arange(0,25,1)
plot=np.append(plot,plot[0])
plt.plot(x,plot)
plot[:]=mean
plt.plot(x,plot)
x=np.arange(0.,24.1,0.1)
plt.plot(x,mean+a*np.cos(2.*pi*x/24.)+b*np.sin(2.*pi*x/24.))
plt.xlabel("UTC")
plt.ylabel("Precipitation rate [mm/h]")
plt.xlim(0,24)
#plt.locator_params(axis="x",tight=True,nbins=10)
plt.savefig("fourier.png")

