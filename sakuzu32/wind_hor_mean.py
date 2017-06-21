#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import *

#########################
lon1=70.
lon2=160.
lat1=-15.
lat2=30.
grid=0.75
##############################

##############################
#かきたいえのsize
#########################

#test rectangle
#lon3=96.
#lon4=101.
#lat3=-5.
#local=7


#new guinia
#lon3=135.
#lon4=145.
#lat3=-10.

#local=7
#
#smatrawest
#lon3=93.
#lon4=96.
#lat3=4.
#local=7
#wide=12.
#dire="smwest"

#sm east
#lon3=100.
#lon4=103.
#lat3=0.
#local=7
#wide=9
#dire="smeast"

#ng east
#lon3=142.
#lon4=144.
#lat3=-3.
#wide=11
#local=9
#dire="ng"



#br west
#lon3=116.
#lon4=118.
#lat3=6.
#wide=8. #grid の倍数に
#dire="brwest"

#ng west
#lon3=135.
#lon4=137.
#lat3=-5
#local=9

#br east
#lon3=116.
#lon4=120.
#lat3=-1.
#lat4=7.
#dire="breast"
#wide=7.5 #grid の倍数に

#mean
lon3=90.
lon4=130.
lat3=-2.
lat4=2.
local=7
dire="mean"


level=[100,125,150,175,200,225,250,300,350,400,450,500,550,600,650,700,750,775,800,825,850,875,900,925,950,975,1000]

levelnum=len(level)
hournum=4


#length=lon4-lon3

#lat4=lat3+length

lon1num=int(lon1/grid)+1
lat1num=int((90.-lat1)/grid)
lon2num=int(lon2/grid)
lat2num=int((90.-lat2)/grid)+1
print lon1num,lon2num,lat1num,lat2num
lonsize=lon2num-lon1num+1
latsize=lat1num-lat2num+1

lon3num=int(lon3/grid)-int(lon1/grid)
lon4num=int(lon4/grid)+1-int(lon1/grid)
lat3num=int((90.-lat3)/grid)-int((90.-lat2)/grid)-1
lat4num=int((90.-lat4)/grid)-int((90.-lat2)/grid)
#widenum=int(wide/grid)

#print lon3num,lon4num,lat3num,lat4num,widenum

umean=np.load("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu31/winddata_wh041213/uphase1.npy")
vmean=np.load("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu31/winddata_wh041213/vphase1.npy")

umean=umean*0.
vmean=vmean*0.

#for phase in range(1,5):
count=0
#for phase in [1,2,3,8]:
#	title="Easterly"

for phase in [4,5,6,7]:
	title="Westerly"
	u=np.load("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu31/winddata_wh041213/uphase"+str(phase)+".npy")
	v=np.load("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu31/winddata_wh041213/vphase"+str(phase)+".npy")
	umean+=u
	vmean+=v
	print np.shape(u)


	#umean=np.zeros((hournum,levelnum))
	#vmean=np.zeros((hournum,levelnum))

	count+=1

umean=umean/count
vmean=vmean/count





umean=umean[:,:,lat4num:lat3num+1,lon3num:lon4num+1]
vmean=vmean[:,:,lat4num:lat3num+1,lon3num:lon4num+1]
count=0

umean=umean.mean(axis=(0,2,3))
vmean=vmean.mean(axis=(0,2,3))

plotwind=umean

ax=plt.gca()
ax.invert_yaxis()
plt.yscale("log")
ax.set_yticks([100,200,300,400,500,600,700,800,900,1000])	
ax.yaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_minor_formatter(FormatStrFormatter("%d"))
ax.yaxis.set_minor_locator(FixedLocator([100,200,300,400,500,600,700,800,900,1000]))	
plt.xlim(-25.,6.)
plt.xlabel("Wind Speed [m/s]")
plt.ylabel("Level [hPa]")
plt.plot(plotwind,level)
plt.title(title)
plt.savefig("figure/wh04_"+dire+"/wind/"+title+".png")
#plt.show()
plt.clf()			



