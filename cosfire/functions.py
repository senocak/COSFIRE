from sklearn.base import BaseEstimator, TransformerMixin
from .base import FunctionFilter

class CircularPeaksFunction(FunctionFilter):
    def __init__(self):
        super().__init__(_circularPeaks)

class NormalizeFunction(FunctionFilter):
    def __init__(self):
        super().__init__(_normalize)

# Function to find maxima in a circular array
# Returns: array of indices
def _circularPeaks(array):
    n = len(array)
    up = array[0] > array[n-1]
    maxima = []
    for i, val in enumerate(array):
        #i = i[0]
        added = False
        if i == n-1:
            if up and array[0] < val:
                maxima.append(i)
                added = True
        else:
            if up and (array[i+1] < val):
                maxima.append(i)
                added = True
                up = not up
            elif not up and (array[i+1] > val):
                up = not up
    return maxima

def _normalize(image):
    image -= image.min()
    return image/image.max()