from core.agility.v3_3.agilitymodel.base.ServiceProviderType import ServiceProviderTypeBase
from core.agility.v3_3.agilitymodel.actions.ServiceProviderType import ServiceProviderTypeActions

class ServiceProviderType(ServiceProviderTypeBase, ServiceProviderTypeActions):
    '''
    classdocs
    '''
    def __init__(self, sdkservice=False, supertype=[], servicetypesupertype=[], option=[], adapter=None, servicetype=[]):
        '''
        Constructor
        @param sdkservice: sdkservice
        @type sdkservice: boolean
        @param supertype: supertype minOccurs=0 maxOccurs=unbounded
        @type supertype: Link
        @param servicetypesupertype: servicetypesupertype minOccurs=0 maxOccurs=unbounded
        @type servicetypesupertype: Link
        @param option: option minOccurs=0 maxOccurs=unbounded
        @type option: ServiceProviderOption
        @param adapter: adapter minOccurs=0
        @type adapter: string
        @param servicetype: servicetype minOccurs=0 maxOccurs=unbounded
        @type servicetype: Link
        '''
        ServiceProviderTypeBase.__init__(self, sdkservice=sdkservice, supertype=supertype, servicetypesupertype=servicetypesupertype, option=option, adapter=adapter, servicetype=servicetype)
