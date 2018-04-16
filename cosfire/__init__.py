from .template import (TemplateEstimator, TemplateClassifier,
                       TemplateTransformer)

from .base import (FunctionFilter, gaussianFilter)

__all__ = ['TemplateEstimator', 'TemplateClassifier',
           'TemplateTransformer', 'FunctionFilter', 'gaussianFilter']
