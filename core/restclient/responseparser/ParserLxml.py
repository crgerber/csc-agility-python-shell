'''
Created on Oct 15, 2012

@author: dawood
'''

##################### XML to/from dict ########################

# Create python xml structures compatible with
# http://search.cpan.org/~grantm/XML-Simple-2.18/lib/XML/Simple.pm
from common import *
from LxmlTools import etree, xml2d, d2xml, assetToXMLTemplate

import copy

COMPONENT_NAME = 'XML_PARSER_Lxml'
from logger import getLogger
logger = getLogger(COMPONENT_NAME)


@persist
def parse(xmlText, assetType=None, removeNSPrefix=True):
    '''
    parses xmlText using lxml library into composite of smart objects
    
    @param xmlText: xml text to parse
    @param assetType: type of first level asset(s) in the xmlText
    @param removeNSPrefix: if True, ns prefix will be removed from xml tag names, default to True
    @return: composite of AbstractProxy object graph 
    '''
    if not xmlText:
        return xmlText
    
    e = etree.XML(xmlText)
    dct = xml2d(e, removeNSPrefix)
    k, v = dct.items().pop()
    if k not in TAG_HIERARCHIES_MAP:
        return AssetEntryLxml(dct, assetType)
    else:
        childTag = TAG_HIERARCHIES_MAP.get(k, None) or k[:k.find('list')]
        #Note: in apiv2.0, some services return Scriptlist, Templatelist tags, for example the search API's
        return [AssetEntryLxml({assetType : e}, assetType) for e in v.get(childTag, [])]

class ProxyLxml(AbstractProxy):
    def _load(self, key):
        item = self._attrs[key]
        if isinstance(item, (str, unicode)):
            item = decode(item)
        elif isinstance(item, dict):
            item = self._newSubObject(item)
        elif isinstance(item, list):
            if len(item) == 1:
                item = item.pop()
                if isinstance(item, dict):
                    if item:
                        item = self._newSubObject(item) #else subitem is a dict or a simple str, otherwise undefined behaviour
                    else:#empty child tag, return simple empty string
                        item = ''
            else:
                item = [self._newSubObject(subitem) for subitem in item]#will result in a list of a mixture of subobjects and strings
        else:
            raise RuntimeError('Unexpected attribute value type: %(key)s : %(item)s, type: %(itemtype)s'%{'key': key, 'item' : item, 'itemtype': type(item)})
        return item
    
    def _newSubObject(self, attrs):
        return AssetAttributeLxml(attrs) if isinstance(attrs, dict) else decode(attrs)#attrs are either a dictionary, in such case a subobject should be created, or a unicode/str value -> returned as str

class AssetAttributeLxml(ProxyLxml):
    def __init__(self, attrs):
        assert(isinstance(attrs, dict))
        AbstractProxy.__init__(self, attrs)
        self._topLevel = False
        self._autoattrs += ['_dct']
        self._dct = copy.deepcopy(attrs)#stash a copy of the native dict
        [self._attrs.update([(key, self._load(key))]) for key in self._attrs.keys()]


class AssetEntryLxml(ProxyLxml):
    def __init__(self, dct, assetName=None):
        '''        
        example input param = {'Script': {'creator': [{'name': ['admin'], 'href': ['https://localhost:8443/agility/api/current/user/1'], 'rel': ['up'], 'position': ['0'], 'type': ['application/com.servicemesh.agility.api.User+xml'], 'id': ['1']}], 'runAsAdmin': ['false'], 'id': ['104'], 'assetType': [{'name': ['script'], 'href': ['https://localhost:8443/agility/api/current/assettype/2'], 'rel': ['up'], 'position': ['0'], 'type': ['application/com.servicemesh.agility.api.AssetType+xml'], 'id': ['2']}], 'assetPath': ['/Root/SHADOW/Project101'], 'uuid': ['ba93106a-da1f-4c26-8a46-940556842bb7'], 'top': ['false'], 'version': ['-1'], 'removable': ['true'], 'type': ['Guest'], 'description': ['Test Script for Test Bench Development'], 'parent': [{'name': ['Project101'], 'href': ['https://localhost:8443/agility/api/current/project/29'], 'rel': ['up'], 'position': ['0'], 'type': ['application/com.servicemesh.agility.api.Project+xml'], 'id': ['29']}], 'enableExtensions': ['false'], 'lockType': ['0'], 'publisher': [{'name': ['admin'], 'href': ['https://localhost:8443/agility/api/current/user/1'], 'rel': ['up'], 'position': ['0'], 'type': ['application/com.servicemesh.agility.api.User+xml'], 'id': ['1']}], 'name': ['TEST SCRIPT 102'], 'created': ['2012-10-15T00:46:52-04:00'], 'lastModified': ['2012-10-15T00:46:52-04:00'], 'lifecycleVersion': ['-1'], 'timeout': ['3600'], 'operatingSystem': ['Unknown'], 'latest': ['false']}}
        '''
        assert(len(dct) == 1)
        k, v = dct.items().pop()
        assert(isinstance(v, dict))#if v is a list, a LinkList response is being passed as xmlText
        
        AbstractProxy.__init__(self, v, assetName or k)
        self._topLevel = True
        self._autoattrs += ['_dct']
        self._dct = copy.deepcopy(dct)#stash a copy of the native dict
        [self._attrs.update([(key, self._load(key))]) for key in self._attrs.keys()]
        pass#just to set a break point here
        
    def _getXmlText(self):
        return d2xml(self._dct)
    
    def _createTemplate(self, *deleteVars, **substituteVars):
        '''
        creates an xml string template for the asset at hand, that can be used to invoke further REST APIs
        
        @param deleteVars: var args list of 
        '''
        #remove id, uuid, date created, last modified
        xmlheader = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>"""
        templateVars = {}
        template =  d2xml(self._dct, favourAttributes=False, returnNode=True, templatise=True, templateVars=templateVars)
        template.set('xmlns', 'http://servicemesh.com/agility/api')
        template = xmlheader + etree.tostring(template)
        for key in templateVars:
            if key in deleteVars:
                templateVars[key] = ''
            elif key in substituteVars:
                templateVars[key] = substituteVars[key]
            
        return template, templateVars
    
    def createXMLTemplate(self, deleteFields=None, replaceFields=None):
        return assetToXMLTemplate(self, deleteFields, replaceFields)

'''
def basicTests():
    attributedXML = """<module xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" uri="test">
       <gobject xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" type="xx" name="g"/>
       <tag name="a" value="b"/>
       <tag name="c" value="d"/>
       <script lang="python">CDATA</script>
    </module>"""
    nestedXML = """<module>
        <uri>test</uri>
        <gobject name="g">
            <type>xx</type>
        </gobject>
        <tag>
            <name>a</name>
            <value>b</value>
        </tag>
        <tag>
            <name>c</name>
            <value>d</value>
        </tag>
        <script>
            <lang>python</lang>
            <body>CDATA</body>
        </script>
        <repo>
            <location>
                <t>here</t>
                <t>righthere</t>
            </location>
            <location>there</location>
        </repo>
        <repo>
            <location>somewhere</location>
            <location>somewhereelse</location>
        </repo>
    </module>"""
    print attributedXML
    d1 = xml2d(etree.XML(attributedXML))
    print d1
    attributedXML_gen1 = d2xml(d1, favourAttributes=True)
    print attributedXML_gen1
    nestedXML_gen1 = d2xml(d1, favourAttributes=False)
    print nestedXML_gen1
    
    print nestedXML
    d2 = xml2d(etree.XML(nestedXML))
    print d2
    attributedXML_gen2 = d2xml(d2, favourAttributes=True)
    print attributedXML_gen2
    templateVars = {}
    nestedXML_gen2 = d2xml(d2, favourAttributes=False)
    print nestedXML_gen2
    nestedXML_gen3 = d2xml(d2, favourAttributes=False, templatise=True, templateVars=templateVars)
    print nestedXML_gen3
    print templateVars
    print nestedXML_gen3%templateVars

def convertToObjectsTest():
    dctAsset = {'Script': {'creator': [{'name': ['admin'], 'href': ['https://localhost:8443/agility/api/current/user/1'], 'rel': ['up'], 'position': ['0'], 'type': ['application/com.servicemesh.agility.api.User+xml'], 'id': ['1']}], 'runAsAdmin': ['false'], 'id': ['104'], 'assetType': [{'name': ['script'], 'href': ['https://localhost:8443/agility/api/current/assettype/2'], 'rel': ['up'], 'position': ['0'], 'type': ['application/com.servicemesh.agility.api.AssetType+xml'], 'id': ['2']}], 'assetPath': ['/Root/SHADOW/Project101'], 'uuid': ['ba93106a-da1f-4c26-8a46-940556842bb7'], 'top': ['false'], 'version': ['-1'], 'removable': ['true'], 'type': ['Guest'], 'description': ['Test Script for Test Bench Development'], 'parent': [{'name': ['Project101'], 'href': ['https://localhost:8443/agility/api/current/project/29'], 'rel': ['up'], 'position': ['0'], 'type': ['application/com.servicemesh.agility.api.Project+xml'], 'id': ['29']}], 'enableExtensions': ['false'], 'lockType': ['0'], 'publisher': [{'name': ['admin'], 'href': ['https://localhost:8443/agility/api/current/user/1'], 'rel': ['up'], 'position': ['0'], 'type': ['application/com.servicemesh.agility.api.User+xml'], 'id': ['1']}], 'name': ['TEST SCRIPT 102'], 'created': ['2012-10-15T00:46:52-04:00'], 'lastModified': ['2012-10-15T00:46:52-04:00'], 'lifecycleVersion': ['-1'], 'timeout': ['3600'], 'operatingSystem': ['Unknown'], 'latest': ['false']}}
    dctAssetList = {'LinkList' : [
                         {'link': [{'name': ['Apache ActiveMQ 5.5.0 Install'],
    'href': ['https://localhost:8443/agility/api/current/script/1'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['1']},
    {'name': ['MySQL 5.5 x86_64'], 'href':
    ['https://localhost:8443/agility/api/current/script/2'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['2']},
    {'name': ['MySQL 5.5 i386'], 'href':
    ['https://localhost:8443/agility/api/current/script/3'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['3']},
    {'name': ['Rabbit MQ Install'], 'href':
    ['https://localhost:8443/agility/api/current/script/4'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['4']},
    {'name': ['Apache Zookeeper 3.3.3 Install'], 'href':
    ['https://localhost:8443/agility/api/current/script/5'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['5']},
    {'name': ['Join Active Directory Domain'], 'href':
    ['https://localhost:8443/agility/api/current/script/6'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['6']},
    {'name': ['Join Active Directory Domain'], 'href':
    ['https://localhost:8443/agility/api/current/script/7'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['7']},
    {'name': ['agility-svc-mgr.sh'], 'href':
    ['https://localhost:8443/agility/api/current/script/8'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['8']},
    {'name': ['Start Detection Install'], 'href':
    ['https://localhost:8443/agility/api/current/script/9'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['9']},
    {'name': ['Start Detection Config'], 'href':
    ['https://localhost:8443/agility/api/current/script/10'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['10']},
    {'name': ['Agility Monitor Install'], 'href':
    ['https://localhost:8443/agility/api/current/script/11'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['11']},
    {'name': ['Agility Monitor Config'], 'href':
    ['https://localhost:8443/agility/api/current/script/12'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['12']},
    {'name': ['Agility Monitor Install'], 'href':
    ['https://localhost:8443/agility/api/current/script/13'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['13']},
    {'name': ['Agility Monitor Config'], 'href':
    ['https://localhost:8443/agility/api/current/script/14'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['14']},
    {'name': ['Agility Monitor Install'], 'href':
    ['https://localhost:8443/agility/api/current/script/15'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['15']},
    {'name': ['Start Detection Install'], 'href':
    ['https://localhost:8443/agility/api/current/script/17'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['17']},
    {'name': ['Agility Monitor Config'], 'href':
    ['https://localhost:8443/agility/api/current/script/16'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['16']},
    {'name': ['Agility Secure'], 'href':
    ['https://localhost:8443/agility/api/current/script/19'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['19']},
    {'name': ['Start Detection Config'], 'href':
    ['https://localhost:8443/agility/api/current/script/18'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['18']},
    {'name': ['Agility Secure Unregister'], 'href':
    ['https://localhost:8443/agility/api/current/script/21'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['21']},
    {'name': ['Agility Secure Status'], 'href':
    ['https://localhost:8443/agility/api/current/script/20'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['20']},
    {'name': ['Agility Secure Status'], 'href':
    ['https://localhost:8443/agility/api/current/script/23'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['23']},
    {'name': ['Agility Secure'], 'href':
    ['https://localhost:8443/agility/api/current/script/22'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['22']},
    {'name': ['Agility Secure'], 'href':
    ['https://localhost:8443/agility/api/current/script/25'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['25']},
    {'name': ['Agility Secure Unregister'], 'href':
    ['https://localhost:8443/agility/api/current/script/24'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['24']},
    {'name': ['Agility Secure Unregister'], 'href':
    ['https://localhost:8443/agility/api/current/script/27'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['27']},
    {'name': ['Agility Secure Status'], 'href':
    ['https://localhost:8443/agility/api/current/script/26'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['26']},
    {'name': ['EC2Bundle-Linux'], 'href':
    ['https://localhost:8443/agility/api/current/script/29'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['29']},
    {'name': ['Install ClamWin on Windows'], 'href':
    ['https://localhost:8443/agility/api/current/script/28'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['28']},
    {'name': ['EC2Bundle-Solaris'], 'href':
    ['https://localhost:8443/agility/api/current/script/31'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['31']},
    {'name': ['EC2Bundle-Windows'], 'href':
    ['https://localhost:8443/agility/api/current/script/30'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['30']},
    {'name': ['reconfig'], 'href':
    ['https://localhost:8443/agility/api/current/script/34'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['34']},
    {'name': ['ext3'], 'href':
    ['https://localhost:8443/agility/api/current/script/35'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['35']},
    {'name': ['mount'], 'href':
    ['https://localhost:8443/agility/api/current/script/32'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['32']},
    {'name': ['umount'], 'href':
    ['https://localhost:8443/agility/api/current/script/33'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['33']},
    {'name': ['umount xfs'], 'href':
    ['https://localhost:8443/agility/api/current/script/38'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['38']},
    {'name': ['thaw'], 'href':
    ['https://localhost:8443/agility/api/current/script/39'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['39']},
    {'name': ['xfs'], 'href':
    ['https://localhost:8443/agility/api/current/script/36'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['36']},
    {'name': ['mount xfs'], 'href':
    ['https://localhost:8443/agility/api/current/script/37'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['37']},
    {'name': ['mount'], 'href':
    ['https://localhost:8443/agility/api/current/script/42'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['42']},
    {'name': ['umount'], 'href':
    ['https://localhost:8443/agility/api/current/script/43'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['43']},
    {'name': ['freeze'], 'href':
    ['https://localhost:8443/agility/api/current/script/40'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['40']},
    {'name': ['zfs'], 'href':
    ['https://localhost:8443/agility/api/current/script/41'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['41']},
    {'name': ['umount'], 'href':
    ['https://localhost:8443/agility/api/current/script/46'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['46']},
    {'name': ['reconfig'], 'href':
    ['https://localhost:8443/agility/api/current/script/47'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['47']},
    {'name': ['ntfs'], 'href':
    ['https://localhost:8443/agility/api/current/script/44'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['44']},
    {'name': ['mount'], 'href':
    ['https://localhost:8443/agility/api/current/script/45'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['45']},
    {'name': ['Reboot Instance'], 'href':
    ['https://localhost:8443/agility/api/current/script/51'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['51']},
    {'name': ['useradd'], 'href':
    ['https://localhost:8443/agility/api/current/script/50'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['50']},
    {'name': ['useradd'], 'href':
    ['https://localhost:8443/agility/api/current/script/49'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['49']},
    {'name': ['useradd'], 'href':
    ['https://localhost:8443/agility/api/current/script/48'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['48']},
    {'name': ['Squid Unconfig'], 'href':
    ['https://localhost:8443/agility/api/current/script/55'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['55']},
    {'name': ['Squid Config'], 'href':
    ['https://localhost:8443/agility/api/current/script/54'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['54']},
    {'name': ['Squid el5 i386'], 'href':
    ['https://localhost:8443/agility/api/current/script/53'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['53']},
    {'name': ['oscheck'], 'href':
    ['https://localhost:8443/agility/api/current/script/52'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['52']},
    {'name': ['Agility Common Components Install'], 'href':
    ['https://localhost:8443/agility/api/current/script/59'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['59']},
    {'name': ['Squid el6 x86_64'], 'href':
    ['https://localhost:8443/agility/api/current/script/58'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['58']},
    {'name': ['Squid el6 i386'], 'href':
    ['https://localhost:8443/agility/api/current/script/57'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['57']},
    {'name': ['Squid el5 x86_64'], 'href':
    ['https://localhost:8443/agility/api/current/script/56'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['56']},
    {'name': ['Agility Collector Install'], 'href':
    ['https://localhost:8443/agility/api/current/script/63'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['63']},
    {'name': ['Agility Service Stop'], 'href':
    ['https://localhost:8443/agility/api/current/script/62'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['62']},
    {'name': ['Agility Service Start'], 'href':
    ['https://localhost:8443/agility/api/current/script/61'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['61']},
    {'name': ['Agility Common Components Config'], 'href':
    ['https://localhost:8443/agility/api/current/script/60'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['60']},
    {'name': ['Agility Database Replication'], 'href':
    ['https://localhost:8443/agility/api/current/script/68'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['68']},
    {'name': ['Agility Database Backup'], 'href':
    ['https://localhost:8443/agility/api/current/script/69'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['69']},
    {'name': ['Agility Promote To Master'], 'href':
    ['https://localhost:8443/agility/api/current/script/70'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['70']},
    {'name': ['Agility Web Install'], 'href':
    ['https://localhost:8443/agility/api/current/script/71'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['71']},
    {'name': ['Agility Collector Config'], 'href':
    ['https://localhost:8443/agility/api/current/script/64'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['64']},
    {'name': ['Agility Collector Upgrade'], 'href':
    ['https://localhost:8443/agility/api/current/script/65'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['65']},
    {'name': ['Agility Server Install'], 'href':
    ['https://localhost:8443/agility/api/current/script/66'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['66']},
    {'name': ['Agility Server Config'], 'href':
    ['https://localhost:8443/agility/api/current/script/67'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['67']},
    {'name': ['Agility Node IPSec Config'], 'href':
    ['https://localhost:8443/agility/api/current/script/76'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['76']},
    {'name': ['Tomcat Install'], 'href':
    ['https://localhost:8443/agility/api/current/script/77'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['77']},
    {'name': ['Tomcat Deploy'], 'href':
    ['https://localhost:8443/agility/api/current/script/78'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['78']},
    {'name': ['Tomcat Start'], 'href':
    ['https://localhost:8443/agility/api/current/script/79'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['79']},
    {'name': ['Agility Web Config'], 'href':
    ['https://localhost:8443/agility/api/current/script/72'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['72']},
    {'name': ['Agility Worker Install'], 'href':
    ['https://localhost:8443/agility/api/current/script/73'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['73']},
    {'name': ['Agility Worker Config'], 'href':
    ['https://localhost:8443/agility/api/current/script/74'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['74']},
    {'name': ['Agility Node IPSec Init'], 'href':
    ['https://localhost:8443/agility/api/current/script/75'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['75']},
    {'name': ['Copy of BikiScriptDev'], 'href':
    ['https://localhost:8443/agility/api/current/script/87'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['87']},
    {'name': ['Tomcat Undeploy'], 'href':
    ['https://localhost:8443/agility/api/current/script/81'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['81']},
    {'name': ['Tomcat Stop'], 'href':
    ['https://localhost:8443/agility/api/current/script/80'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['80']},
    {'name': ['BikiScriptDev'], 'href':
    ['https://localhost:8443/agility/api/current/script/82'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['82']},
    {'name': ['testscript'], 'href':
    ['https://localhost:8443/agility/api/current/script/93'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['93']},
    {'name': ['install101'], 'href':
    ['https://localhost:8443/agility/api/current/script/95'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['95']},
    {'name': ['download101'], 'href':
    ['https://localhost:8443/agility/api/current/script/94'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['94']},
    {'name': ['BikiScriptTest'], 'href':
    ['https://localhost:8443/agility/api/current/script/89'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['89']},
    {'name': ['Test-ES'], 'href':
    ['https://localhost:8443/agility/api/current/script/91'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['91']},
    {'name': ['Copy of BikiScriptTest'], 'href':
    ['https://localhost:8443/agility/api/current/script/90'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['90']},
    {'name': ['Install Agility Platform'], 'href':
    ['https://localhost:8443/agility/api/current/script/102'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['102']},
    {'name': ['Install S3cmd Tool'], 'href':
    ['https://localhost:8443/agility/api/current/script/103'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['103']},
    {'name': ['Download Agility Binaries'], 'href':
    ['https://localhost:8443/agility/api/current/script/101'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['101']},
    {'name': ['hellopyunit'], 'href':
    ['https://localhost:8443/agility/api/current/script/98'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['98']},
    {'name': ['Install Agility Base'], 'href':
    ['https://localhost:8443/agility/api/current/script/99'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['99']},
    {'name': ['start101'], 'href':
    ['https://localhost:8443/agility/api/current/script/96'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['96']},
    {'name': ['TESTBENCH SCRIPT 103'], 'href':
    ['https://localhost:8443/agility/api/current/script/106'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['106']},
    {'name': ['TEST SCRIPT 102'], 'href':
    ['https://localhost:8443/agility/api/current/script/104'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['104']},
    {'name': ['TEST SCRIPT 102'], 'href':
    ['https://localhost:8443/agility/api/current/script/105'], 'rel':
    ['self'], 'position': ['0'], 'type':
    ['application/com.servicemesh.agility.api.Script+xml'], 'id': ['105']}]}]
           }
'''    
    
if __name__=="__main__":
    basicTests()
