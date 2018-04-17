import numpy
from PIL import Image
import matplotlib.pyplot as plt
import cosfire
import numpy as np
import math as m

imgColor = numpy.asarray(Image.open('tomato.jpg').convert('RGB'))
filt = cosfire.GaborFilter(1, 0, 2, 1, 0.5*m.pi)
img = numpy.asarray(Image.open('tomato.jpg').convert('L'))
img = filt.fit().transform(img)
plt.imshow(img, cmap='gray')
plt.show()