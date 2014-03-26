from core.agility.v3_0.agilitymodel.base.ResourcePolicy import ResourcePolicyBase
from core.agility.v3_0.agilitymodel.actions.ResourcePolicy import ResourcePolicyActions

class ResourcePolicy(ResourcePolicyBase, ResourcePolicyActions):
    '''
    classdocs
    '''
    def __init__(self, trace=None, mapping=[], name=None, apiversion=None, description=None):
        '''
        Constructor
        @param trace: trace
        @type trace: int
        @param mapping: mapping minOccurs=0 maxOccurs=unbounded
        @type mapping: ResourceMapping
        @param name: name minOccurs=0
        @type name: string
        @param apiversion: apiversion minOccurs=0
        @type apiversion: string
        @param description: description minOccurs=0
        @type description: string
        '''
        ResourcePolicyBase.__init__(self, trace=trace, mapping=mapping, name=name, apiversion=apiversion, description=description)
