from base.ServiceBinding import ServiceBindingBase
from actions.ServiceBinding import ServiceBindingActions

class ServiceBinding(ServiceBindingBase, ServiceBindingActions):
    '''
    classdocs
    '''
    def __init__(self, serviceId=None, type=None, properties=list()):
        '''
        Constructor
        @param serviceId: serviceId minOccurs=0
        @type serviceId: string
        @param type: type minOccurs=0
        @type type: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        '''
        ServiceBindingBase.__init__(self, serviceId=serviceId, type=type, properties=properties)
