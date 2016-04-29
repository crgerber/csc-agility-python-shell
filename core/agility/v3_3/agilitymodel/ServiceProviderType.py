from core.agility.v3_3.agilitymodel.base.ServiceProviderType import ServiceProviderTypeBase
from core.agility.v3_3.agilitymodel.actions.ServiceProviderType import ServiceProviderTypeActions

class ServiceProviderType(ServiceProviderTypeBase, ServiceProviderTypeActions):
    '''
    classdocs
    '''
    def __init__(self, servicetypesupertype=[], sdkservice=False, servicetype=[], option=[], adapter=None, supertype=[]):
        '''
        Constructor
        @param servicetypesupertype: servicetypesupertype minOccurs=0 maxOccurs=unbounded
        @type servicetypesupertype: Link
        @param sdkservice: sdkservice
        @type sdkservice: boolean
        @param servicetype: servicetype minOccurs=0 maxOccurs=unbounded
        @type servicetype: Link
        @param option: option minOccurs=0 maxOccurs=unbounded
        @type option: ServiceProviderOption
        @param adapter: adapter minOccurs=0
        @type adapter: string
        @param supertype: supertype minOccurs=0 maxOccurs=unbounded
        @type supertype: Link
        '''
        ServiceProviderTypeBase.__init__(self, servicetypesupertype=servicetypesupertype, sdkservice=sdkservice, servicetype=servicetype, option=option, adapter=adapter, supertype=supertype)
