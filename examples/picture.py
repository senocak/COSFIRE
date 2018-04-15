import numpy
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('rhino.png').convert('L')
print(numpy.asarray(img))

plt.imshow(img, cmap='gray')
plt.show()