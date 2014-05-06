'''
Created on Dec 14, 2012

@author: dawood
'''
import re

from agilityshell import agility
from core.http.put.localarchive import LocalArchive as archive

__all__ = ['archive']


#backup = '''%(docHeader)s<%(typeName)s xmlns="http://servicemesh.com/agility/api">
#    <name>%(name)s</name>
#    <description>%(description)s</description>%(attributes)s
#</%(typeName)s>'''
def createTemplate(typeName, **kwargs):
    docHeaderTemplate = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'''
    docHeader = '%s\n'%docHeaderTemplate
    template = '''%(docHeader)s<%(typeName)s xmlns="http://servicemesh.com/agility/api">
    %(attributes)s
</%(typeName)s>'''
    sep = ''
    attributes = ''
    if kwargs:
        for key, value in kwargs.iteritems():
            attributes += sep + '<%(key)s>%(value)s</%(key)s>'%{'key' : key, 'value' : value}
            sep = '\n    '
        
    return template%{'docHeader' : docHeader, 'typeName' : typeName, 'attributes' : attributes}

def getTypeName(obj):
    typeName = ''
    typeUrl = obj.get('type', None)
    TYPE_NAME = 'TYPE_NAME'
    if typeUrl:
        match = re.match('application/com\.servicemesh\.agility\.api\.(?P<TYPE_NAME>.*)\+xml', typeUrl)
        typeName = match.groupdict()[TYPE_NAME]
    return typeName


def loadDetails(assetSummary):
    referenceAttrs = ['type', 'href']
    typeName = getTypeName(assetSummary)
    href = getattr(assetSummary, 'href', None)
    if typeName and href:
        result = agility.tools.xml.parse(agility.cfg.conn.request(href), assetType=typeName)
    else:
        raise ValueError('Attributes %s must be set'%referenceAttrs)