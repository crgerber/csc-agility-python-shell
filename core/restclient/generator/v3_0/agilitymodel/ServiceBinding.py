from base.ServiceBinding import ServiceBindingBase
from actions.ServiceBinding import ServiceBindingActions

class ServiceBinding(ServiceBindingBase, ServiceBindingActions):
    '''
    classdocs
    '''
    def __init__(self, serviceid=None, type=None, properties=[]):
        '''
        Constructor
        @param serviceid: serviceid minOccurs=0
        @type serviceid: string
        @param type: type minOccurs=0
        @type type: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        '''
        ServiceBindingBase.__init__(self, serviceid=serviceid, type=type, properties=properties)
