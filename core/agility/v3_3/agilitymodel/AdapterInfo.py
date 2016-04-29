from core.agility.v3_3.agilitymodel.base.AdapterInfo import AdapterInfoBase
from core.agility.v3_3.agilitymodel.actions.AdapterInfo import AdapterInfoActions

class AdapterInfo(AdapterInfoBase, AdapterInfoActions):
    '''
    classdocs
    '''
    def __init__(self, category='', dependencies=[], version='', description='', symbolicname='', vendor='', name=''):
        '''
        Constructor
        @param category: category
        @type category: string
        @param dependencies: dependencies minOccurs=0 maxOccurs=unbounded
        @type dependencies: PackageInfo
        @param version: version
        @type version: string
        @param description: description
        @type description: string
        @param symbolicname: symbolicname
        @type symbolicname: string
        @param vendor: vendor
        @type vendor: string
        @param name: name
        @type name: string
        '''
        AdapterInfoBase.__init__(self, category=category, dependencies=dependencies, version=version, description=description, symbolicname=symbolicname, vendor=vendor, name=name)
