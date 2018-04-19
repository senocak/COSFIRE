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
rhoList = [0,20,40]
(cx, cy) = (50,50)
tuples = []
tupleCoords = []
precision = 16
peakFunction = cosfire.CircularPeaksFunction()
for rho in rhoList:
	if rho == 0:
		if protoDoG[cy,cx] > 0:
			tuples.append((sigma, rho, 0))
			tupleCoords.append((cy, cx));
	elif rho > 0:
		# Compute points (amount=precision) on the circle of radius rho with center point (cx,cy)
		coords = [ ( cy+int(round(rho*m.sin(phi))) , cx+int(round(rho*m.cos(phi))) )
					for phi in
						[i*m.pi/precision*2 for i in range(0,precision)]
				 ]
		vals = [protoDoG[coord] for coord in coords]

		# Find peaks in circle
		maxima = peakFunction.transform(vals)
		tuples.extend([ (sigma, rho, i*m.pi/precision*2) for i in maxima])
		tupleCoords.extend([ coords[i] for i in maxima])

print("Tuples:")
for tupl in tuples:
	print(tupl)

# Draw image
plt.imshow(protoDoG, cmap='gray')
tupleCoords = np.asarray(tupleCoords)
plt.plot(tupleCoords[:,1], tupleCoords[:,0],"xr")
plt.show()
