from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
from PIL import Image
import math as m
import scipy.signal as signal
import scipy.ndimage.filters as scipyfilter

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

def gaussianFilter(image, sigma):
    return filters.gaussian_filter(image, sigma);

def differenceOfGaussians(image, sigma, onoff, sigmaRatio=0.5):

    sz = m.ceil(sigma*3)*2 + 1;
    kernel1 = np.zeros((sz,sz));
    kernel1[sz//2,sz//2] = 1;
    kernel1 = scipyfilter.gaussian_filter(kernel1, sigma);

    kernel2 = np.zeros((sz,sz));
    kernel2[sz//2,sz//2] = 1;
    kernel2 = scipyfilter.gaussian_filter(kernel1, sigma*sigmaRatio);

    if (onoff):
        kernel = kernel2 - kernel1;
    else:
        kernel = kernel1 - kernel2;

    return signal.convolve(image, kernel, mode='same');

def normalize(image):
    image -= image.min();
    return image/image.max();
