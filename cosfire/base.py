from sklearn.base import BaseEstimator, TransformerMixin
import math as m
import cv2
import scipy.signal as signal

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

    def Guassian(sigma):
        kernel = cv2.getGaussianKernel(m.ceil(sigma*3)*2 + 1, sigma)
        return FunctionFilter(_sepFilter2D, kernel)

    def DoG(sigma, onoff, sigmaRatio=0.5):
        sz = m.ceil(sigma*3)*2 + 1;   # Guaranteed to be odd
        kernel1 = cv2.getGaussianKernel(sz, sigma)
        kernel2 = cv2.getGaussianKernel(sz, sigma*sigmaRatio)
        if (onoff):
            kernel = kernel2 - kernel1
        else:
            kernel = kernel1 - kernel2
        return FunctionFilter(_sepFilter2D, kernel)

    def Gabor(sigma, theta, lambd, gamma, psi):
        sz = m.ceil(sigma*3)*2 + 1;   # Guaranteed to be odd
        kernel = cv2.getGaborKernel((sz, sz), sigma, theta, lambd, gamma, psi);
        return FunctionFilter(_Filter2D, kernel);

# Executes a 2D convolution by using a 1D kernel twice
def _sepFilter2D(image, kernel):
    return cv2.sepFilter2D(image, -1, kernel, kernel)

# Executes a 2D convolution by using a 2D kernel
def _Filter2D(image, kernel):
    return signal.convolve(image, kernel, mode='same')

def normalize(image):
    image -= image.min()
    return image/image.max()