'''
Created on Apr 23, 2013

@author: dawood
'''
__all__ = ['new', 'asSubType']

from modelgenerator import agilitymodel as new

def asSubType(modelInstance, subType=None, nested=True, namespace=''):
    sep = ':' if namespace else ''
    xsi_attrs = {'__xsi_nsmap__' : {'xsi': 'http://www.w3.org/2001/XMLSchema-instance'},
    '__xsi_type__' : '%s%s%s'%(namespace, sep, subType if subType else modelInstance.__class__.__name__)}
    modelInstance._topLevel = not nested
    for attrName, attrVal in xsi_attrs.items():
        setattr(modelInstance, attrName, attrVal)
    return modelInstance 