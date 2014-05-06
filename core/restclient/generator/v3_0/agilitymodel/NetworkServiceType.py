from base.NetworkServiceType import NetworkServiceTypeBase
from actions.NetworkServiceType import NetworkServiceTypeActions

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
