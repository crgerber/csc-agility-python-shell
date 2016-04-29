from core.agility.v3_3.agilitymodel.base.PlatformService import PlatformServiceBase
from core.agility.v3_3.agilitymodel.actions.PlatformService import PlatformServiceActions

class PlatformService(PlatformServiceBase, PlatformServiceActions):
    '''
    classdocs
    '''
    def __init__(self, topology=None, properties=[], login=None, blueprint=None, type=None):
        '''
        Constructor
        @param topology: topology minOccurs=0
        @type topology: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param login: login minOccurs=0
        @type login: Credential
        @param blueprint: blueprint minOccurs=0
        @type blueprint: Link
        @param type: type minOccurs=0
        @type type: Link
        '''
        PlatformServiceBase.__init__(self, topology=topology, properties=properties, login=login, blueprint=blueprint, type=type)
