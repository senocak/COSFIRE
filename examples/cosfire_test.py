from PIL import Image
from peakutils.peak import indexes
import matplotlib.pyplot as plt
import cosfire
import numpy as np
import math as m
import time

proto = np.asarray(Image.open('prototype1.png').convert('L'), dtype=np.float64)

sigma = 2.6
filt = cosfire.DoGFilter(sigma,1)
protoDoG = filt.transform(proto)

# Suppress
maxVal = protoDoG.max()
for (x,y), value in np.ndenumerate(protoDoG):
	protoDoG[x,y] = 0 if value < 0.25*maxVal else value;

# Hacky function to find maxima in a circular array
def getMaxima(vals):
	n = vals.size
	circle = np.concatenate([vals,vals,vals])
	index = indexes(circle, thres=0.2, min_dist=0)
	maxima = []
	for i in range(index.size):
		if index[i] >= n and index[i] < n*2:
			maxima.append((2*m.pi/n) * (index[i]-n))
	return maxima

# Find tuples
rhoList = [0,10,20,40]
(cx, cy) = (50,50)
maximaCoords = []
numDegrees = 16
for rho in rhoList:
	if rho == 0:
		if protoDoG[cy,cx] > 0.2:
			print((sigma, rho, 0))
			maximaCoords.append([cx, cy])
	elif rho > 0:
		vals = np.zeros(numDegrees)
		for i in range(0,numDegrees):
			x = m.floor(cx + rho*m.cos(i*m.pi/numDegrees*2))
			y = m.floor(cy + rho*m.sin(i*m.pi/numDegrees*2))
			vals[i] = protoDoG[y,x]
		maxima = getMaxima(vals)
		for phi in maxima:
			print((sigma, rho, phi))
			maximaCoords.append([cx + rho*m.cos(phi), cy + rho*m.sin(phi)])

# Draw image
plt.imshow(protoDoG, cmap='gray')
maximaCoords = np.asarray(maximaCoords)
plt.plot(maximaCoords[:,0], maximaCoords[:,1],"xr")
plt.show()
