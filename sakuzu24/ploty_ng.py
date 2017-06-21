#coding:utf-8
import sys
sys.path.append('/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu09/')

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from function import *
import os.path
import matplotlib.cm as cm
#####################
#fileのサイズ
#########################
lon1=70.
lon2=160.
lat1=-15.
lat2=30.
grid=0.1
##############################
#かきたいえのsize
#########################
#lon3=108.
#lon4=120
#lat3=-5
#lat4=8

#lon3=94.
#lon4=107
#lat3=-7
#lat4=6

#lon3=93.
#lon4=155.
#lat3=-12.
#lat4=8.

#new g
lon3=130
lon4=153
lat3=-12
lat4=0

##############################

nstart=int((lon3-lon1)/grid)
nend=int((lon4-lon1)/grid)
mstart=int((lat3-lat1)/grid)
mend=int((lat4-lat1)/grid)
print "mstart:",mstart,"mend:",mend,"nstart:",nstart,"nend:",nend

lon=np.arange(lon1,lon2+grid,grid)
lat=np.arange(lat1,lat2+grid,grid)
lonp=np.arange(lon3,lon4+grid,grid)
latp=np.arange(lat3,lat4+grid,grid)

msize,nsize=getsize(lon,lat)
mpsize,npsize=getsize(lonp,latp)
print "msize:",msize,"nsize:",nsize
print "mpsize:",mpsize,"npsize:",npsize
print "len(lonp):",len(lonp),"len(latp):",len(latp)



for i in range(1,9):


    plotcp=np.zeros((npsize,mpsize))


    ###################################################
    plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu24/plotdata/dailyp"+"%02d"%i+".dat",delimiter=",")
    #plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu22/plotdata/meanphi.dat",delimiter=",")
    #######################################################


    print np.shape(plotdata)


    #################
    #CUT
    ################
    plotcp=plotdata[mstart:mend+1,nstart:nend+1]
    print "plotcp:",np.shape(plotcp)


    m = Basemap(projection='merc', llcrnrlat=lat3, urcrnrlat=lat4,llcrnrlon=lon3, urcrnrlon=lon4, resolution='l')
    #resolution l m h
    m.drawcoastlines(linewidth=1.5,color='black')
    m.drawparallels(np.arange(lat3-1,lat4,1.),labels=[True,False,False,True])    #緯線
    m.drawmeridians(np.arange(lon3-2,lon4,4.),labels=[False,True,False,True])  #経線


    X, Y = np.meshgrid(lonp,latp)
    x, y = m(X, Y)  

    ###########################################################



    m.contourf(x, y, plotcp,np.arange(0,2.1,0.1),cmap=cm.afmhot_r)
    #m.contourf(x, y, plotcp)
    #m.contourf(x, y, plotcp,np.arange(0,25,1))
    m.colorbar()
    output="figure/bimodal_ng/daily"+"%02d"%i+".png"
    #output="figure/meanphi.png"
    #plt.title("Phase of Diurnal Precipitation in MJO [UTC]")
    plt.title("Precipitation Rate in MJO  [Phase="+"%02d"%i+"]  [mm/h]")
    
	###########################################################


    plt.savefig(output,transparent=True)
    print output
    #plt.show()

    plt.clf()


os.system("convert -delay 80 -loop 0 figure/bimodal_ng/*.png bimodal_ng_daily.gif")
