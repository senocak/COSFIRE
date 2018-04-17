import numpy
from PIL import Image
import matplotlib.pyplot as plt
import scipy.signal as signal
import cosfire as cosf
import numpy as np

filt = cosf.FunctionFilter(cosf.differenceOfGaussians, 1.5, 0.5);
img = numpy.asarray(Image.open('tomato.jpg').convert('L'))
imgColor = numpy.asarray(Image.open('tomato.jpg').convert('RGB'))
img = filt.fit().transform(img);
img = cosf.normalize(img);

avg = np.average(img);
for (x,y), value in np.ndenumerate(img):
	img[x,y] = 0 if value < avg else 1;

#print(img);
#print(imgColor);

imgRes = numpy.zeros(shape = imgColor.shape)

'''
for (x,y,c), value in np.ndenumerate(imgColor):
	temp = imgColor[x,y,:];
	imgRes[x,y] = temp;

#imgColor = imgColor * img;
#print(imgRes);
#print(imgColor);
'''

imgRes[:,:,:] = (imgColor[:,:,:]/255);
imgRes[:,:,0] = imgRes[:,:,0]*img[:,:];
imgRes[:,:,1] = imgRes[:,:,1]*img[:,:];
imgRes[:,:,2] = imgRes[:,:,2]*img[:,:];

plt.imshow(imgRes);
plt.show()