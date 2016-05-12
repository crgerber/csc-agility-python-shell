from core.agility.v3_3.agilitymodel.base.ServiceBinding import ServiceBindingBase
from core.agility.v3_3.agilitymodel.actions.ServiceBinding import ServiceBindingActions

class ServiceBinding(ServiceBindingBase, ServiceBindingActions):
    '''
    classdocs
    '''
    def __init__(self, type=None, serviceid=None, properties=[]):
        '''
        Constructor
        @param type: type minOccurs=0
        @type type: Link
        @param serviceid: serviceid minOccurs=0
        @type serviceid: string
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        '''
        ServiceBindingBase.__init__(self, type=type, serviceid=serviceid, properties=properties)