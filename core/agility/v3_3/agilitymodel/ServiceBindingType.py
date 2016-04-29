from core.agility.v3_3.agilitymodel.base.ServiceBindingType import ServiceBindingTypeBase
from core.agility.v3_3.agilitymodel.actions.ServiceBindingType import ServiceBindingTypeActions

class ServiceBindingType(ServiceBindingTypeBase, ServiceBindingTypeActions):
    '''
    classdocs
    '''
    def __init__(self, properties=[], platformservicetype=None):
        '''
        Constructor
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param platformservicetype: platformservicetype minOccurs=0
        @type platformservicetype: Link
        '''
        ServiceBindingTypeBase.__init__(self, properties=properties, platformservicetype=platformservicetype)
