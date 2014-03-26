'''
Created on Nov 19, 2012

@author: dawood
'''
from functools import partial
import re
from core.base.enum import Enum
from core.pyworx.text import validSymbol, isValidSymbol, validPythonSymbol, isValidPythonSymbol
import logger
import types
import datetime
from dateutil.parser import parse as parseISODate

logger = logger.getLogger(__name__)

def modelObjectTypes():
    '''
    A trick to defer importing the model modules to break the cyclic import
    '''
    from core.restclient.responseparser.common import AbstractProxy
    from core.agility.common.AgilityModelBase import AgilityModelBase
    from core import agility
    return AbstractProxy, AgilityModelBase

############# type agnostic property access funcs ############# 

################ attribute name filtering ################
privateFilter = lambda name: not name.startswith('_')

callableFilter = lambda obj, attr: not isinstance(getattr(obj, attr), (types.FunctionType, types.MethodType))

################ type agnostic property access ################
listFields = lambda item: item.keys() if isinstance(item, dict) else filter(privateFilter, dir(item))#filter(partial(callableFilter, item), filter(privateFilter, dir(item)))

getField = lambda item, field, default=None: item.get(field, default) if isinstance(item, dict) else getattr(item, field, default)

setField = lambda item, field, value: item.update([(field, value)]) if isinstance(item, dict) else setattr(item, field, value)

hasField = lambda item, field: field in item if isinstance(item, dict) else hasattr(item, field)

################ prefix search, ideally for use with flattened maps to find groups of child attributes ################
listFieldsWithPrefix = lambda item, prefix, flatten=False: filter(lambda f: f.startswith(prefix), listFields(flattenmap(item) if flatten else item))

getFieldsWithPrefix = lambda item, prefix, flatten=False: map(partial(getField, flattenmap(item) if flatten else item), listFieldsWithPrefix(item, prefix, flatten))

selectFieldsWithPrefix = lambda item, prefix, flatten=False: dict(zip(listFieldsWithPrefix(item, prefix, flatten), getFieldsWithPrefix(item, prefix, flatten)))

################ suffix search, simply because we can find them ################
listFieldsWithSuffix = lambda item, suffix, flatten=False: filter(lambda f: f.endswith(suffix), listFields(flattenmap(item) if flatten else item))

getFieldsWithSuffix = lambda item, suffix, flatten=False: map(partial(getField, flattenmap(item) if flatten else item), listFieldsWithSuffix(item, suffix, flatten))

selectFieldsWithSuffix = lambda item, prefix, flatten=False: dict(zip(listFieldsWithSuffix(item, prefix, flatten), getFieldsWithSuffix(item, prefix, flatten)))

################ regex search within attribute names ################
listFieldsWithRegex = lambda item, pattern, flatten=False: [k for k in listFields(flattenmap(item) if flatten else item) if re.match(pattern, k)]

getFieldsWithRegex = lambda item, pattern, flatten=False: map(partial(getField, flattenmap(item) if flatten else item), listFieldsWithRegex(item, pattern, flatten))
    
selectFieldsWithRegex = lambda item, pattern, flatten=False: dict(zip(listFieldsWithRegex(item, pattern, flatten), getFieldsWithRegex(item, pattern, flatten)))

################ regex search within attribute values ################
listFieldsWithValueRegex = lambda item, pattern, flatten=True: [k for k, v in (flattenmap(item) if flatten else selectFields(item)).items() if re.match(pattern, str(v))] 

getFieldsWithValueRegex = lambda item, pattern, flatten=True:  map(partial(getField, flattenmap(item) if flatten else item), listFieldsWithValueRegex(item, pattern, flatten))

selectFieldsWithValueRegex = lambda item, pattern, flatten=True: dict(zip(listFieldsWithValueRegex(item, pattern, flatten), getFieldsWithValueRegex(item, pattern, flatten)))

################ apply filter on attribute values ################
listFieldsWithValueFilter = lambda item, filterfunc, flatten=True: [k for k, v in (flattenmap(item) if flatten else selectFields(item)).items() if filterfunc(v)] 

getFieldsWithValueFilter = lambda item, filterfunc, flatten=True:  map(partial(getField, flattenmap(item) if flatten else item), listFieldsWithValueFilter(item, filterfunc, flatten))

selectFieldsWithValueFilter = lambda item, filterfunc, flatten=True: dict(zip(listFieldsWithValueFilter(item, filterfunc, flatten), getFieldsWithValueFilter(item, filterfunc, flatten)))

    
################ regex listing resulted in a field, get its parent sub-object easily using the fully qualified name a.b.c.d ################
def getParentField(item, fieldFQN, relation=1, useIndex=False):
    levels = fieldFQN.split('.')
    if relation > len(levels):
        raise ValueError('Invalid value for relation [%s] must be < depth of FQN')
    elif relation == len(levels):
        return item
    attr = None
    parent = item
    for idx in range(len(levels)-relation):
        level = levels[idx]
        attr = getField(parent, level, None)
        if attr is None: raise KeyError('No such field [%s]'%fieldFQN)
        if isinstance(attr, (list, tuple)):
            parent = idmap(attr, 'id', defaultToIndex=True, useIndex=useIndex)
        else:
            parent = attr 
    return attr

def popField(item, fieldFQN, nestedById=True):
    return modField(item, fieldFQN, pop=True, nestedById=nestedById)

def replaceField(item, fieldFQN, newvalue, nestedById=True):
    return modField(item, fieldFQN, pop=False, newvalue=newvalue, nestedById=nestedById)    

def modField(item, fieldFQN, pop=True, newvalue=None, nestedById=True):
    '''
    @param pop: pop or replace, default True
    @param newvalue: if replace, field value is replaces by newvalue
    '''
    field = None
    levels = fieldFQN.split('.')
    fieldName = levels[-1]
    parent = getParentField(item, fieldFQN, relation=1, useIndex=(not nestedById))
    if parent is None: raise KeyError('No such field [%s]'%fieldFQN)
    if isinstance(parent, (list, tuple)):
        if nestedById and all(map(lambda item: hasField(item, 'id'), parent)):
            id = fieldName
            for idx, item in enumerate(parent):
                if id == getField(item, 'id'):
                    if pop:
                        field = parent.pop(idx)
                    else:
                        parent[idx] = newvalue
        else:
            idx = int(fieldName)
            if pop:
                field = parent.pop(idx)
            else:
                parent[idx] = newvalue
    else:
        if pop:
            field = getField(parent, fieldName)
            if field is None: raise KeyError('No such field [%s]'%fieldFQN)
            del parent[fieldName]
        else:
            parent[fieldName] = newvalue
    return field

def idmap(itemList, keyField='id', defaultToIndex=False, useIndex=False):
    '''
    transforms a list of objects OR maps into a map with keyField extracted from each item as key to this item. keyField value is assumed to be unique across the set
    
    @param itemList: sequence of Objects or Dicts
    @param keyField: name of the item's field to be used as key for this item
    @param defaultToIndex: use a sequential index as key if keyField doesn't exist in ALL items
    '''
    if not useIndex:
        withids = filter(lambda item: hasField(item, keyField), itemList)
        if len(withids) < len(itemList): 
            if not defaultToIndex:
                logger.warn('idmap() : some items do not have [%s] field', keyField)
                raise AttributeError('idmap() : some items do not have an [id] field')
            else:
                useIndex = True
    result = {}
    try:
        [result.update([(getField(asset, keyField) if not useIndex else str(index) , asset)]) for index, asset in enumerate(itemList)]
    except AttributeError, ex:
        logger.error('Invalid keyField: %s', ex)
        raise
    return result

namemap = lambda itemlist: idmap(itemlist, keyField='name', defaultToIndex=False)

def flattenmap(dct, parentKey='', includeComposites=True):
    '''
    converts a proxy object or a dictionary to a one level flat map, with field fully qualified names as keys
    
    @param dct: proxy object or dictionary
    @param parentKey: initial value for parent key, mainly used in recursion
    @param includeComposites: include a key for a value that is a list of objects + include key.objectID. If false, only leaf nodes are included
    '''
    if isinstance(dct, modelObjectTypes()):
        dct = selectFields(dct, fields=None)
        
    flatmap = {}
    for k, v in dct.items():
        if isinstance(v, (dict, modelObjectTypes())):
            if includeComposites:
                flatmap['%s%s%s'%(parentKey,'.' if parentKey else '', k)] = v
            flatmap.update(flattenmap(v, '%s%s%s'%(parentKey,'.' if parentKey else '', k)))
        elif isinstance(v, (tuple, list)):
            if includeComposites:
                flatmap['%s%s%s'%(parentKey,'.' if parentKey else '', k)] = v
            if all([isinstance(item, (dict, modelObjectTypes())) for item in v]):#list of composite types
                if includeComposites:
                    [flatmap.update([('%s%s%s.%s'%(parentKey,'.' if parentKey else '', k, item[0]), item[1])]) for item in idmap(v, keyField='id', defaultToIndex=True).items()]#include keys for key.objectID
                [flatmap.update(flattenmap(item[1], '%s%s%s.%s'%(parentKey,'.' if parentKey else '',k, item[0]))) for item in idmap(v, keyField='id', defaultToIndex=True).items()]#include leafs of ke.objectID
            else:
                [flatmap.update([('%s%s%s.%s'%(parentKey,'.' if parentKey else '', k, item[0]), item[1])]) for item in idmap(v, keyField='id', defaultToIndex=True).items()]
        else:
            flatmap['%s%s%s'%(parentKey,'.' if parentKey else '', k)] = v
    return flatmap


SELECT_FIELDS_MATCH = Enum(**dict(PREFIX='prefix',
                            SUFFIX='suffix',
                            REGEX='regex'))

def selectFields(item, fields=None, factory=dict, ignore=False, default=None, match=SELECT_FIELDS_MATCH.PREFIX, flatten=False):
    '''
    selects a subset of dict (key, value) pairs or object attribute (name, value) pairs
    behaves differently from selectFieldsWith[Prefix, Suffix, Regex] is that it selects the set of fields as provided in the args 
    in addition to expanding the field set with the matched fields, which is more suitable for reports since it will preserve the columns provided, and expand on them if applicable
    For example: 
    fields = ['id', 'name', 'properties'] and match=SUFFIX
    the result field map will include:
    {'id' : <value>, 'name' : <value>, 'properties' : <value>, 'properties.type' : <value>, 'properties.id' : <value>, ...}
    
    @param item: dictionary or arbitrary python object
    @param fields: list of key/attribute names, None => all
    @param factory: callable factory method used to instantiate a result placeholder, default to dict
    @param ignore: if True, ignore the fields that don't correspond to a key or attribute, else keep the keys and set value to <default>
    @param default: default value for missing keys/attributes if ignore=False
    @param prefixMatch: if True, will include item attributes starting with <field> for each field in <fields>, idealy used with flattened composite objects/maps to find sub groups
    @param suffixMatch: if True, will include item attributes ending with <field> for each field in <fields>, idealy used with flattened composite objects/maps to find grand children
    @param flatten: if True, the object/map will be flattened
    '''
    global a
    if fields is None:
        fields = listFields(item)
    result = factory()
    expandedFields = list(fields)#copy
    if flatten:
        item = flattenmap(item)
    
    matcher = {SELECT_FIELDS_MATCH.PREFIX : listFieldsWithPrefix,
               SELECT_FIELDS_MATCH.SUFFIX : listFieldsWithSuffix,
               SELECT_FIELDS_MATCH.REGEX : listFieldsWithRegex}
    if flatten:
        [expandedFields.extend(matcher[match](item, field, flatten)) for field in fields]
    
    #remove the matched fields from the item before running the exact match logic next
    [setField(result, field, getField(item, field, default)) for field in expandedFields if (hasField(item, field) or (not ignore))]
    return result

selectFields.MATCH = SELECT_FIELDS_MATCH

def modifyMap(dct, deleteFields=None, replaceFields=None):
    '''
    @fields: list of FQN field names, you can generate a list of Fully Qualified Field Names by using scripting.flattenmap(dict)
    ''' 
    if deleteFields is None: deleteFields = []
    if replaceFields is None: replaceFields = {}
    flatmap = flattenmap(dct, '')
    for fieldToDelete in sorted(deleteFields):
        try:
            popField(dct, fieldToDelete)
        except KeyError, ex:
            logger.warn(ex)
    for fieldToReplace, newvalue in replaceFields.items():
        replaceField(dct, fieldToReplace, newvalue)
    
    return dct

isodateNow = lambda: datetime.datetime.now().isoformat()
isodateParse = lambda datestring: parseISODate(datestring)
