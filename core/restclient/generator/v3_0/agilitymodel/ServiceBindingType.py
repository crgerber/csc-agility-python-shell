from base.ServiceBindingType import ServiceBindingTypeBase
from actions.ServiceBindingType import ServiceBindingTypeActions

class ServiceBindingType(ServiceBindingTypeBase, ServiceBindingTypeActions):
    '''
    classdocs
    '''
    def __init__(self, platformservicetype=None, properties=[]):
        '''
        Constructor
        @param platformservicetype: platformservicetype minOccurs=0
        @type platformservicetype: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        '''
        ServiceBindingTypeBase.__init__(self, platformservicetype=platformservicetype, properties=properties)
