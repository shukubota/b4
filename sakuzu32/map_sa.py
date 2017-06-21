#coding:utf-8
import sys
sys.path.append('/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu09/')

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from function import *
import os.path
import matplotlib.cm as cm

##############################
#かきたいえのsize
#########################
#smatra
#lon3=92.
#lon4=110
#lat3=-7
#lat4=8


#south america
lon3=-110.
lon4=-65.
lat3=-10.
lat4=20.


#br
#lon3=108.
#lon4=121
#lat3=-5
#lat4=9


#maritime
#lon3=93.
#lon4=155.
#lat3=-12.
#lat4=8.

#lon3=70.
#lon4=160.
#lat3=-15.
#lat4=30.


#test
#lon3=0.
#lon4=359.
#lat3=-80
#lat4=80

#1 naname 2 horizontal

#smwest
which=1

rlon3=-86.
rlon4=-71.
rlat3=-3.
wide=10.

#smatrawest
r2lon3=116.
r2lon4=120.
r2lat3=1.
r2lat4=7.


#lon4=96.
#lat3=4.
#br east
#which=2
#rlon3=115.
#rlon4=119.
#rlat3=-1.
#rlat4=7.



m = Basemap(projection='merc', llcrnrlat=lat3, urcrnrlat=lat4,llcrnrlon=lon3, urcrnrlon=lon4, resolution='l')
#resolution l m h
m.drawcoastlines(linewidth=1.5,color='black')
m.drawparallels(np.arange(lat3,lat4,2.),labels=[True,False,False,True])    #緯線
m.drawmeridians(np.arange(lon3,lon4,5.),labels=[False,True,False,True])	#経線


#lonp=123
#latp=0
#X, Y = np.meshgrid(lonp,latp)

if which==1:
	x1, y1 = m(rlon3, rlon4-rlon3+rlat3)
	x2, y2 = m(rlon4, rlat3)
	x4, y4 = m(rlon3-wide*0.5*np.sqrt(2.), rlon4-rlon3+rlat3-wide*0.5*np.sqrt(2.))
	x3, y3 = m(rlon4-wide*0.5*np.sqrt(2.), rlat3-wide*0.5*np.sqrt(2.))

	
elif which==2:
	x1,y1=m(rlon3,rlat3)
	x2,y2=m(rlon3,rlat4)
	x3,y3=m(rlon4,rlat4)
	x4,y4=m(rlon4,rlat3)
	
	
	

#print x1,y1

#print m(123)
#m.plot([x1,y1], [x2 ,y2])
xtrack = [x1,x2,x3,x4,x1]
ytrack = [y1,y2,y3,y4,y1]
m.plot(xtrack, ytrack,color="black",lw=3)

#xtrack = [xe1,xe2,xe3,xe4,xe1]
#ytrack = [ye1,ye2,ye3,ye4,ye1]
#m.plot(xtrack, ytrack,color="black",lw=3)

output="figure/map_sa.png"
plt.savefig(output,bbox_inches="tight")


