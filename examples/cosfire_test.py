from PIL import Image
from peakutils.peak import indexes
import matplotlib.pyplot as plt
import cosfire
import numpy as np
import math as m
import time

proto = np.asarray(Image.open('prototype4.png').convert('L'), dtype=np.float64)

sigma = 2.6
filt = cosfire.DoGFilter(sigma,1)
protoDoG = filt.transform(proto)

# Suppress
maxVal = protoDoG.max()
for (x,y), value in np.ndenumerate(protoDoG):
	protoDoG[x,y] = 0 if value < 0.25*maxVal else value;

# Find tuples
rhoList = [0,10,20,40]
(cx, cy) = (50,50)
maximaCoords = []
numDegrees = 16
peakFunction = cosfire.CircularPeaksFunction()
for rho in rhoList:
	if rho == 0:
		if protoDoG[cy,cx] > 0:
			maximaCoords.append([cx, cy])
	elif rho > 0:
		vals = [protoDoG[m.floor(cy + rho*m.sin(i*m.pi/numDegrees*2)),m.floor(cx + rho*m.cos(i*m.pi/numDegrees*2))] for i in range(0,numDegrees)]
		maxima = peakFunction.transform(vals)
		maximaCoords.extend([[cx + rho*m.cos(phi*m.pi/numDegrees*2), cy + rho*m.sin(phi*m.pi/numDegrees*2)] for phi in maxima])

# Draw image
plt.imshow(protoDoG, cmap='gray')
maximaCoords = np.asarray(maximaCoords)
plt.plot(maximaCoords[:,0], maximaCoords[:,1],"xr")
plt.show()
