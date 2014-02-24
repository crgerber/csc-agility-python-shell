'''
Created on Oct 15, 2012

@author: dawood
'''
from common import *
from bs4 import BeautifulSoup
COMPONENT_NAME = 'XML_PARSER_BeautifulSoup'
from logger import getLogger
logger = getLogger(COMPONENT_NAME)


class ProxyBeautifulSoup(AbstractProxy):
    
    def _loadAll(self, entrySoup, attrNameFilter, loadAttrs=False):
        #first load any attributes, decode key and value to ascii and strip white spaces
        attrs = {}
        if loadAttrs:
            for attrK, attrV in entrySoup.attrs.items():
                attrK = decode(attrK).strip()
                if attrK.startswith('xmlns') : continue
                attrK = attrK[attrK.find(':')+1:]#remove NameSpace prefix
                attrs[attrK] = decode(attrV).strip()
            
        #filter out '\n' elements resulting from pretty printing the XML
        #NOTE: only exists on first level of the DOM tree, multiline CDATA content are intact as "text" property of an enclosing Tag  element
        #@todo: check if BeautifulSoup API's can filter out new lines automatically
        
        children = filter(lambda e: decode(e).strip(), entrySoup.children)
        for child in children:
            key = attrNameFilter(child.name)
            if key not in attrs:
                attrs[key] = self._load(child)
            else:
                values = attrs[key]
                if not isinstance(values, list): values = [values]
                values.append(self._load(child))
                attrs[key] = values
                
        return attrs
    
    def _load(self, entrySoup):
        if len(entrySoup.contents) <= 1:#empty tag or a text field
            try:
                text = decode(entrySoup.text)
            except UnicodeEncodeError, ex:
                logger.warn('Failed to convert %s to string, error details: %s', entrySoup.text, ex)
                text = entrySoup.text
            return text.strip()
        return self._newSubObject(entrySoup)
    
    def _newSubObject(self, attrs):
        return AssetAttributeBeautifulSoup(attrs)
    
class AssetAttributeBeautifulSoup(ProxyBeautifulSoup):
    def __init__(self, entrySoup, attrNameFilter=lambda n: n):
        attrs = self._loadAll(entrySoup, attrNameFilter)
#        self.__dict__.update(attrs)
        AbstractProxy.__init__(self, attrs)
    
class AssetEntryBeautifulSoup(ProxyBeautifulSoup):
    def __init__(self, entrySoup, assetType, attrNameFilter=lambda n: n):
        attrs = self._loadAll(entrySoup, attrNameFilter)
        AbstractProxy.__init__(self, attrs, typeName=assetType)
        self._autoattrs += ['_rawXML']
        self._rawXML =  entrySoup.prettify()
        
    def _getXmlText(self):
        return self._rawXML
        
def linklistToAssetEntryList(soup, assetType='generic'):
    result = []
    parentlist = None
    selectedHierarchy = ''
    for tagh in TAG_HIERARCHIES:
        parentlist = soup.find(tagh[0])
        if parentlist:
            selectedHierarchy = tagh
            break
    if not parentlist:
        return result
    links = parentlist.find_all(selectedHierarchy[1])#link or Asset
    result = [AssetEntryBeautifulSoup(link, assetType) for link in links]
    return result

def parseSingleAsset(soup, assetType='generic', attrNameFilter=lambda n: n):
    """
    Parse a single asset response from Agility REST APIs
    
    @param soup: BeauitfulSoup object, containing the response xml document
    @param assetType: asset name, will be only used if the asset name could not be extracted from the response
    @param attrNameFilter: function to manipulate asset name and asset attribute names if required, 
    e.g. in case of parsing the document as html, remove the 'ns1:' prefix
    @return: AssetEntryBeautifulSoup object, populated with all attributes
    """
    entry = soup.contents[0]
    actualAssetType = getattr(entry, 'name', None)
    actualAssetType = attrNameFilter(actualAssetType) if actualAssetType else assetType
    result = AssetEntryBeautifulSoup(entry, actualAssetType, attrNameFilter)
    return result

@persist
def parse(xmlText, assetType, removeNSPrefix=True):
    '''
    parses xmlText using BeautifulSoup library into composite of smart objects
    
    @param xmlText: xml text to parse
    @param assetType: type of first level asset(s) in the xmlText
    @param removeNSPrefix: if True, ns prefix will be removed from xml tag names, default to True
    @return: composite of AbstractProxy object graph 
    '''
    if not xmlText:
        return xmlText
    
    soup = BeautifulSoup(xmlText, 'xml')
    parentlist = None
    for tagh in TAG_HIERARCHIES:
        parentlist = soup.find(tagh[0])
        if parentlist:
            selectedHierarchy = tagh
            break
    if not parentlist:
        return parseSingleAsset(soup, assetType)
    else:
        return linklistToAssetEntryList(soup, assetType)
        
    
    