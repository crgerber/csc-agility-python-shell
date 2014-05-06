from core.agility.v3_0.agilitymodel.base.NetworkServiceType import NetworkServiceTypeBase
from core.agility.v3_0.agilitymodel.actions.NetworkServiceType import NetworkServiceTypeActions

class NetworkServiceType(NetworkServiceTypeBase, NetworkServiceTypeActions):
    '''
    classdocs
    '''
    def __init__(self, services=[], properties=[]):
        '''
        Constructor
        @param services: services minOccurs=0 maxOccurs=unbounded
        @type services: string
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: PropertyDefinition
        '''
        NetworkServiceTypeBase.__init__(self, services=services, properties=properties)
