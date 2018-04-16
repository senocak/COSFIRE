import numpy
from PIL import Image
import matplotlib.pyplot as plt
import scipy.signal as signal
import cosfire as cosf

filt = cosf.FunctionFilter(cosf.gaussianFilter, 1, 1, 0);

img = numpy.asarray(Image.open('rhino.png').convert('L'))

'''
gaus = numpy.matrix(
'2 4 5 4 2;'+
'4 9 12 9 4;'+
'5 12 15 12 5;'+
'4 9 12 9 4;'+
'2 4 5 4 2');
edge = numpy.matrix(
'1 4 1;'+
'4 -20 4;'+
'1 4 1'
);
print(edge);
print(img);
img = signal.convolve(img, edge, mode='same');
'''

img = filt.transform(img);


# Normalization:
#imgTransformed -= imgTransformed.min();
#imgTransformed = imgTransformed/imgTransformed.max();


plt.imshow(img, cmap='gray')
plt.show()