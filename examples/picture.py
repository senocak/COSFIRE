from PIL import Image
import matplotlib.pyplot as plt
import cosfire
import numpy as np
import math as m
import time

proto = np.asarray(Image.open('prototype.png').convert('L'), dtype=np.float64)

filt = cosfire.DoGFilter(2.6,1)
protoDoG = filt.transform(proto)

#print(protoDoG[:,50])

for (x,y), value in np.ndenumerate(protoDoG):
	protoDoG[x,y] = 0 if value < 0 else value;

plt.imshow(protoDoG, cmap='gray')
plt.show()

