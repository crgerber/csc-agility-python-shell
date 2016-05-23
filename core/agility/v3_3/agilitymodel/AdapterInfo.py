from core.agility.v3_3.agilitymodel.base.AdapterInfo import AdapterInfoBase
from core.agility.v3_3.agilitymodel.actions.AdapterInfo import AdapterInfoActions

class AdapterInfo(AdapterInfoBase, AdapterInfoActions):
    '''
    classdocs
    '''
    def __init__(self, vendor='', description='', version='', name='', category='', dependencies=[], symbolicname=''):
        '''
        Constructor
        @param vendor: vendor
        @type vendor: string
        @param description: description
        @type description: string
        @param version: version
        @type version: string
        @param name: name
        @type name: string
        @param category: category
        @type category: string
        @param dependencies: dependencies minOccurs=0 maxOccurs=unbounded
        @type dependencies: PackageInfo
        @param symbolicname: symbolicname
        @type symbolicname: string
        '''
        AdapterInfoBase.__init__(self, vendor=vendor, description=description, version=version, name=name, category=category, dependencies=dependencies, symbolicname=symbolicname)
