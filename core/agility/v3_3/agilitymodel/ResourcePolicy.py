from core.agility.v3_3.agilitymodel.base.ResourcePolicy import ResourcePolicyBase
from core.agility.v3_3.agilitymodel.actions.ResourcePolicy import ResourcePolicyActions

class ResourcePolicy(ResourcePolicyBase, ResourcePolicyActions):
    '''
    classdocs
    '''
    def __init__(self, name=None, description=None, mapping=[], apiversion=None, trace=None):
        '''
        Constructor
        @param name: name minOccurs=0
        @type name: string
        @param description: description minOccurs=0
        @type description: string
        @param mapping: mapping minOccurs=0 maxOccurs=unbounded
        @type mapping: ResourceMapping
        @param apiversion: apiversion minOccurs=0
        @type apiversion: string
        @param trace: trace
        @type trace: int
        '''
        ResourcePolicyBase.__init__(self, name=name, description=description, mapping=mapping, apiversion=apiversion, trace=trace)
