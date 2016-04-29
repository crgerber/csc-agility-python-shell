'''
Created on Apr 22, 2013

@author: dawood
'''
from lxml import etree
from itertools import groupby
from core.pyworx import scripting
import re

CDATA_KEY = '__CDATA__'

def xml2d(e, removeNSPrefix=True, loadAttrs=False):
    """Convert an etree into a dict structure

    @type  e: etree.Element
    @param e: the root of the tree
    @return: The dictionary representation of the XML tree
    """
    def _xml2d(e, loadAttrs=False):
        XSI = 'xsi'
        __xsi_type__ = None
        if loadAttrs:
            nsmap = getattr(e, 'nsmap', {}) #namespace map for the tag/element
            if XSI in nsmap and e.attrib.get('{%s}type'%nsmap.get(XSI, None), None):
                __xsi_type__ = e.attrib.pop('{%s}type'%nsmap[XSI])
                __xsi_nsmap__ = {XSI : nsmap[XSI]}
            kids = {re.sub('\{.*\}', '', attrName) if removeNSPrefix else attrName : attrVal for attrName, attrVal in list(e.attrib.items())}
            if __xsi_type__: 
                kids['__xsi_type__'] = __xsi_type__
                kids['__xsi_nsmap__'] = __xsi_nsmap__
        else:
            kids = {}
        children = e.getchildren()
        for k, g in groupby(children, lambda x: x.tag):
            k = re.sub('\{.*\}', '', k) if removeNSPrefix else k 
            g = [ _xml2d(x, loadAttrs=loadAttrs) for x in g ] 
            kids[k] =  g if len(g) > 1 else g.pop()#remove the if else if side effects occur

        cdata = e.text.strip() if e.text else ''
        if cdata:
            if kids or children:
                kids[CDATA_KEY] = cdata#add cdata under a special key
            else:
                return cdata
#        debug_g = groupby(e, lambda x: x.tag)
#        debug_g = [(t[0], list(t[1])) for t in debug_g]
        return kids
    e = etree.XML(e) if isinstance(e, str) else e
    rootTag = re.sub('\{.*\}', '', e.tag) if removeNSPrefix else e.tag
    return { rootTag : _xml2d(e, loadAttrs=loadAttrs) }    

def d2xml(d, favourAttributes=False, returnNode=False, templatise=False, templateVars=None):
    """convert dict to xml

       1. The top level d must contain a single entry i.e. the root element
       2.  Keys of the dictionary become sublements or attributes
       3.  If a value is a simple string, then the key is an attribute, unless favourAttribute flag is false, a subelement with CDATA content would be emitted
       4.  if a value is dict then, then key is a subelement
       5.  if a value is list, then key is a set of sublements

       a  = { 'module' : {'tag' : [ { 'name': 'a', 'value': 'b'},
                                    { 'name': 'c', 'value': 'd'},
                                 ],
                          'gobject' : { 'name': 'g', 'type':'xx' },
                          'uri' : 'test',
                       }
           }
    >>> d2xml(a, favourAttributes=True)
    <module uri="test">
       <gobject type="xx" name="g"/>
       <tag name="a" value="b"/>
       <tag name="c" value="d"/>
    </module>

    >>> d2xml(a, favourAttributes=False)
    <module>
        <uri>test</uri>
        <gobject>
            <type>xx</type>
            <name>g</name>
        </gobject>
        <tag>
            <name>a</name>
            <value>b</value>
        </tag>
        <tag>
            <name>c</name>
            <value>d</value>
        </tag>
    </module>


    @type  d: dict 
    @param d: A dictionary formatted as an XML document
    @param favourAttributes: if True, children would be formatted as attributes, else nesting is used
    @param returnNode: if True, an etree Node object is returned for further processing, else the node is converted into a string
    @param templatise: if True, a python string template is generated from the xml text, with template variables populated in the templateVars argument
    @param templateVars: if templatise, all template variable key, value paris would be populated into this dictionary 
    @return:  An etree Root element if returnNode, else string
    """
    XSI_TYPE_KEY = '__xsi_type__'
    XSI_NSMAP_KEY = '__xsi_nsmap__'
    XSI = 'xsi'
    def createNode(parent=None, tag=None, xsi_type=None, xsi_nsmap=None):
        node = etree.SubElement(parent, tag, nsmap=xsi_nsmap) if parent is not None else etree.Element(tag, nsmap=xsi_nsmap)
        if xsi_type:
            node.attrib['{%s}type'%xsi_nsmap[XSI]] = xsi_type.split(':')[-1]
        return node
    
    def _d2xml(d, parentNode, favourAttributes, templatise, templateVars):
        def templatiseTag(k, v):
            k = '%s_%s'%(parentNode.getparent().tag, k)
            templateVars[k] = v
            return '%%(%s)s'%k
        
        
        _t = lambda k, v: v
        if templatise:
#            _t = lambda k, v: templateVars.update([(k,v)]) or '%%(%s)s'%k
            _t = templatiseTag
        if isinstance(d, str):
            parentNode.text = _t(parentNode.tag, d)
            return
        for k,v in list(d.items()):
            if isinstance(v,dict):
                xsi_type = v.pop(XSI_TYPE_KEY, None)
                xsi_nsmap = v.pop(XSI_NSMAP_KEY, None)
                node = createNode(parent=parentNode, tag=k, xsi_type=xsi_type, xsi_nsmap=xsi_nsmap)
#                if extractNestedMap and len(v) == 1:
#                    v = v.values()[0]#@todo revisit this logic, add validation that dict at has a type key maybe?
                _d2xml(v, node, favourAttributes=favourAttributes, templatise=templatise, templateVars=templateVars)
            elif isinstance(v,list):
                for item in v:
                    xsi_type = item.pop(XSI_TYPE_KEY, None) if isinstance(item, dict) else None
                    xsi_nsmap = item.pop(XSI_NSMAP_KEY, None) if isinstance(item, dict) else None
                    node = createNode(parent=parentNode, tag=k, xsi_type=xsi_type, xsi_nsmap=xsi_nsmap)
                    _d2xml(item, node, favourAttributes=favourAttributes, templatise=templatise, templateVars=templateVars)
            elif k == CDATA_KEY:#special handling for CDATA values that were parse by the library earlier
                parentNode.text = _t(k, v)
            elif favourAttributes:
                parentNode.set(k, _t(k, v))
            else:
                node = createNode(parent=parentNode, tag=k)
                _d2xml(v, node, favourAttributes=favourAttributes, templatise=templatise, templateVars=templateVars) 

    k,v = list(d.items())[0]
    xsi_type = v.pop(XSI_TYPE_KEY, None) if isinstance(v, dict) else None
    xsi_nsmap = v.pop(XSI_NSMAP_KEY, None) if isinstance(v, dict) else None
    node = createNode(tag=k, xsi_type=xsi_type, xsi_nsmap=xsi_nsmap)#etree.Element(k)
    templateVars = templateVars if templateVars is not None else {}
    _d2xml(v, node, favourAttributes=favourAttributes, templatise=templatise, templateVars=templateVars)
    return node if returnNode else etree.tostring(node)


def assetToXMLTemplate(asset, deleteFields=None, replaceFields=None):
    '''
    creates an xml string template for the asset at hand, that can be used to invoke further REST APIs
    
    @param deleteFields: list of field names to be deleted, fully qualified names can be used, e.f. resources.<id>.network.href
    @param replaceFields: dict of field name, new value pairs
    @return: a tuple containing: template XML string, template dictionary
    '''
    #remove id, uuid, date created, last modified
    if deleteFields is None: deleteFields = []
    if replaceFields is None: replaceFields = {}
    
    xmlheader = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>"""
    templateVars = {}
    dct = eval(repr(asset))
    scripting.modifyMap(dct[asset.typeName], deleteFields=deleteFields, replaceFields=replaceFields)
        
    template =  d2xml(dct, favourAttributes=False, returnNode=True, templatise=False)
    template.set('xmlns', 'http://servicemesh.com/agility/api')
    template = xmlheader + etree.tostring(template)
    return template, dct