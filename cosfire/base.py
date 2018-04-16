from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
from PIL import Image
import math as m
import scipy.signal as signal
import matplotlib.pyplot as plt


class FunctionFilter(BaseEstimator, TransformerMixin):
    """
    A wrapper for filters already available in common image libraries. The signature of those functions must start with
    the image parameter though for this class to be the suitable one.
    Parameters:
    -----------
        filter_function: function
        The filter function wrapped into this class, like gabor, gaussian, etc.
        pargs: Variable length positional parameters
        kwarg: Variable lenght keyword parameters
    """
    def __init__(self, filter_function, *pargs, **kwargs):
        self.filter_function = filter_function
        self.pargs = pargs
        self.kwargs = kwargs

    def fit(self):
        """
        No parameter is learnt by the filter function from the input image so this method is provided just for
        compatibility reasons but it just returns self for chaining convenience.
        """
        return self

    def transform(self, image):
        """
        Transform the input image by applying the filter function provided in the constructor.

        Parameters:
        -----------
            image: image
        """
        return self.filter_function(image, *self.pargs, **self.kwargs)

def gaussianFilter(image, sigmaX, sigmaY, theta):
    
    gaussian = np.zeros(shape=image.shape);
    cx = (gaussian.shape[0]-1)/2;
    cy = (gaussian.shape[1]-1)/2;

    a = (m.cos(theta)**2)/(2*sigmaX*sigmaX) + (m.sin(theta)**2)/(2*sigmaY*sigmaY);
    b = (-m.sin(2*theta))/(4*sigmaX*sigmaX) + (m.sin(2*theta))/(4*sigmaY*sigmaY);
    c = (m.sin(theta)**2)/(2*sigmaX*sigmaX) + (m.cos(theta)**2)/(2*sigmaY*sigmaY);

    for (x,y), value in np.ndenumerate(gaussian) :
        gaussian[x,y] = m.exp(-( (a*(x-cx))**2 + 2*b*(x-cx)*(y-cy) + (c*(y-cy))**2));

    return signal.convolve(image, gaussian, mode='same');
