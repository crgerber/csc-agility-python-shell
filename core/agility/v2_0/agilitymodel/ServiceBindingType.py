from core.agility.v2_0.agilitymodel.base.ServiceBindingType import ServiceBindingTypeBase
from core.agility.v2_0.agilitymodel.actions.ServiceBindingType import ServiceBindingTypeActions

class ServiceBindingType(ServiceBindingTypeBase, ServiceBindingTypeActions):
    '''
    classdocs
    '''
    def __init__(self, platformServiceType=None, properties=list()):
        '''
        Constructor
        @param platformServiceType: platformServiceType minOccurs=0
        @type platformServiceType: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        '''
        ServiceBindingTypeBase.__init__(self, platformServiceType=platformServiceType, properties=properties)
