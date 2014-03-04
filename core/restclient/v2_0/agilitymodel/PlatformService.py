from core.restclient.v2_0.agilitymodel.base.PlatformService import PlatformServiceBase
from core.restclient.v2_0.agilitymodel.actions.PlatformService import PlatformServiceActions

class PlatformService(PlatformServiceBase, PlatformServiceActions):
    '''
    classdocs
    '''
    def __init__(self, blueprint=None, login=None, type=None, properties=list(), topology=None):
        '''
        Constructor
        @param blueprint: blueprint minOccurs=0
        @type blueprint: Link
        @param login: login minOccurs=0
        @type login: Credential
        @param type: type minOccurs=0
        @type type: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param topology: topology minOccurs=0
        @type topology: Link
        '''
        PlatformServiceBase.__init__(self, blueprint=blueprint, login=login, type=type, properties=properties, topology=topology)
