'''
Created on Oct 31, 2012

@author: dawood
'''
class Enum(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        
    def keys(self):
        return list(self.__dict__.keys())

    def values(self):
        return list(self.__dict__.values())
    
    def __repr__(self):
        return str(self.__dict__)
    
    __str__ = __repr__
    