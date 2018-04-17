from sklearn.base import BaseEstimator, TransformerMixin
import math as m
import cv2
import scipy.signal as signal
from .base import FunctionFilter

class GaussianFilter(FunctionFilter):
    def __init__(self, sigma):
        kernel = cv2.getGaussianKernel(m.ceil(sigma*3)*2 + 1, sigma)
        super().__init__(_sepFilter2D, kernel)

class DoGFilter(FunctionFilter):
    def __init__(self, sigma, onoff, sigmaRatio=0.5):
        sz = m.ceil(sigma*3)*2 + 1;   # Guaranteed to be odd
        kernel1 = cv2.getGaussianKernel(sz, sigma)
        kernel2 = cv2.getGaussianKernel(sz, sigma*sigmaRatio)
        if (onoff):
            kernel = kernel2 - kernel1
        else:
            kernel = kernel1 - kernel2
        super().__init__(_sepFilter2D, kernel)

class GaborFilter(FunctionFilter):
    def __init__(self, sigma, theta, lambd, gamma, psi):
        sz = m.ceil(sigma*3)*2 + 1;   # Guaranteed to be odd
        kernel = cv2.getGaborKernel((sz, sz), sigma, theta, lambd, gamma, psi);
        super().__init__(_Filter2D, kernel);

# Executes a 2D convolution by using a 1D kernel twice
def _sepFilter2D(image, kernel):
    return cv2.sepFilter2D(image, -1, kernel, kernel)

# Executes a 2D convolution by using a 2D kernel
def _Filter2D(image, kernel):
    return signal.convolve(image, kernel, mode='same')

def normalize(image):
    image -= image.min()
    return image/image.max()