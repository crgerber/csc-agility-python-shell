from base.ServiceProviderType import ServiceProviderTypeBase
from actions.ServiceProviderType import ServiceProviderTypeActions

class ServiceProviderType(ServiceProviderTypeBase, ServiceProviderTypeActions):
    '''
    classdocs
    '''
    def __init__(self, servicetype=[], option=[], adapter=None, servicetypesupertype=[], sdkservice=False, supertype=[]):
        '''
        Constructor
        @param servicetype: servicetype minOccurs=0 maxOccurs=unbounded
        @type servicetype: Link
        @param option: option minOccurs=0 maxOccurs=unbounded
        @type option: ServiceProviderOption
        @param adapter: adapter minOccurs=0
        @type adapter: string
        @param servicetypesupertype: servicetypesupertype minOccurs=0 maxOccurs=unbounded
        @type servicetypesupertype: Link
        @param sdkservice: sdkservice
        @type sdkservice: boolean
        @param supertype: supertype minOccurs=0 maxOccurs=unbounded
        @type supertype: Link
        '''
        ServiceProviderTypeBase.__init__(self, servicetype=servicetype, option=option, adapter=adapter, servicetypesupertype=servicetypesupertype, sdkservice=sdkservice, supertype=supertype)
