import numpy as np
import sys
from math import *

#Gas conditions
rmm = 78.118 # benzene
ppm = 1.0
temp = 298.15 #in kelvin

#monolayer conditions
apm = 1.7 #nm2/molecule
reten = 1.0 #us

#constants
boltz = 1.38e-23 #m2 kg s-2 k-1
avagad = 6.02e23

#fibre optic surface rea
l = 20.00 #mm
d = 0.15 #mm
sa = 2*pi*(d/2)*l #mm

#gas density
n = ((ppm*40.9)/1000000)*avagad

#number of molecules
TnMol = (sa*1000000000000)/apm

#impacts/retention time unit
mean2speed = 3*boltz*temp/((rmm/avagad)/1000)
meanspeed = pow(((8*mean2speed)/(3*pi)),0.5) #m/s
IperS = 0.25*n*(sa/1000000)*meanspeed
IperRt = IperS*(reten/1000000)

print 'Avliable molecules:'
print "%e" % TnMol
print 
print 'Impacts per second:'
print "%e" % IperS
print 
print 'Impacts within retention time:'
print "%e" % IperRt
print 
print '100% uptake percentage:'
print (IperRt/TnMol)*100
print 

#looper
n=0
CnMol = TnMol
Per = 0
count = 0
IperRtP = IperRt

while (IperRtP > 0):
	if IperRtP > 1000000:
		rn = 1000000
		IperRtP = IperRtP - 1000000
	else:
		rn = IperRtP
		IperRtP = 0
	
	r = np.random.rand(rn) #creates an array of random numbers between 0 and 1
	lenth = len(r)
	countb = 0
	while (countb<lenth):
		RnMol = CnMol/TnMol #number of avliable sites vs the total number
		print round((count/IperRt*100),2)," % complete         \r", #prints percentace complete
		if RnMol > r[countb]: #if RnMol is greater than rand then add an impact to n, removes a impact site
			CnMol = CnMol-1
			n = n+1
			count = count + 1
			countb = countb + 1
		else:
			count = count + 1
			countb = countb + 1

#result impacts within retention time	
print 'Modled random chance uptake percentage'
print n