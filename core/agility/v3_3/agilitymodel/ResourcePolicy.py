from core.agility.v3_3.agilitymodel.base.ResourcePolicy import ResourcePolicyBase
from core.agility.v3_3.agilitymodel.actions.ResourcePolicy import ResourcePolicyActions

class ResourcePolicy(ResourcePolicyBase, ResourcePolicyActions):
    '''
    classdocs
    '''
    def __init__(self, apiversion=None, name=None, trace=None, mapping=[], description=None):
        '''
        Constructor
        @param apiversion: apiversion minOccurs=0
        @type apiversion: string
        @param name: name minOccurs=0
        @type name: string
        @param trace: trace
        @type trace: int
        @param mapping: mapping minOccurs=0 maxOccurs=unbounded
        @type mapping: ResourceMapping
        @param description: description minOccurs=0
        @type description: string
        '''
        ResourcePolicyBase.__init__(self, apiversion=apiversion, name=name, trace=trace, mapping=mapping, description=description)
