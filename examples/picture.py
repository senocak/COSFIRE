import numpy
from PIL import Image
import matplotlib.pyplot as plt
import scipy.signal as signal
import cosfire as cosf
import numpy as np

filt = cosf.FunctionFilter(cosf.differenceOfGaussians, 2, 2, 1);
imgoriginal = numpy.asarray(Image.open('rhino.png').convert('L'))
img = filt.fit().transform(imgoriginal);
img = cosf.normalize(img);

for (x,y), value in np.ndenumerate(img):
	img[x,y] = 0 if value < 0.4 else 1;

print(img);

plt.imshow(img+imgoriginal, cmap='gray')
plt.show()