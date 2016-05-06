from core.agility.v3_3.agilitymodel.base.AdapterInfo import AdapterInfoBase
from core.agility.v3_3.agilitymodel.actions.AdapterInfo import AdapterInfoActions

class AdapterInfo(AdapterInfoBase, AdapterInfoActions):
    '''
    classdocs
    '''
    def __init__(self, category='', symbolicname='', vendor='', name='', version='', dependencies=[], description=''):
        '''
        Constructor
        @param category: category
        @type category: string
        @param symbolicname: symbolicname
        @type symbolicname: string
        @param vendor: vendor
        @type vendor: string
        @param name: name
        @type name: string
        @param version: version
        @type version: string
        @param dependencies: dependencies minOccurs=0 maxOccurs=unbounded
        @type dependencies: PackageInfo
        @param description: description
        @type description: string
        '''
        AdapterInfoBase.__init__(self, category=category, symbolicname=symbolicname, vendor=vendor, name=name, version=version, dependencies=dependencies, description=description)
