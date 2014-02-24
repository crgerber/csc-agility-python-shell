'''
Created on Nov 26, 2012

@author: dawood
'''
from functools import partial
def partially(func, *args):
    partialfunc = partial(func, *args)
    partialfunc.__doc__ = func.__doc__
    partialfunc.__name__ = func.__name__
    return partialfunc