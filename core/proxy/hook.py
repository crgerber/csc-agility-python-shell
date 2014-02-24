'''
Created on Nov 23, 2012

@author: dawood
'''
class Hook(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)