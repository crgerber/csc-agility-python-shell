'''
Created on Nov 19, 2012

@author: dawood
'''
from core.pyworx.text import validSymbol, isValidSymbol
from core.pyworx.scripting import *
import logger
logger = logger.getLogger(__name__)

__all__ = ['idmap', 'namemap', 'selectFields', 'flattenmap', 'listFieldsWithPrefix',\
    'getFieldsWithPrefix', 'listFields', 'getField', 'setField', 'hasField', 'popField', 'replaceField',\
    'listFieldsWithSuffix', 'getFieldsWithSuffix', 'selectFieldsWithPrefix',\
    'selectFieldsWithSuffix', 'listFieldsWithRegex', 'getFieldsWithRegex',\
    'selectFieldsWithRegex', 'listFieldsWithValueRegex', 'getFieldsWithValueRegex',\
    'selectFieldsWithValueFilter', 'listFieldsWithValueFilter', 'getFieldsWithValueFilter',
    'selectFieldsWithValueRegex', 'getParentField', 'validSymbol', 'isValidSymbol', 'validPythonSymbol', 'isValidPythonSymbol',
    'isodateNow', 'isodateParse']
