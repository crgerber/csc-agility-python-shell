from core.agility.v3_3.agilitymodel.base.PlatformService import PlatformServiceBase
from core.agility.v3_3.agilitymodel.actions.PlatformService import PlatformServiceActions

class PlatformService(PlatformServiceBase, PlatformServiceActions):
    '''
    classdocs
    '''
    def __init__(self, topology=None, blueprint=None, properties=[], type=None, login=None):
        '''
        Constructor
        @param topology: topology minOccurs=0
        @type topology: Link
        @param blueprint: blueprint minOccurs=0
        @type blueprint: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param type: type minOccurs=0
        @type type: Link
        @param login: login minOccurs=0
        @type login: Credential
        '''
        PlatformServiceBase.__init__(self, topology=topology, blueprint=blueprint, properties=properties, type=type, login=login)
