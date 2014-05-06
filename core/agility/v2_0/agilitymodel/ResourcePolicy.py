from core.agility.v2_0.agilitymodel.base.ResourcePolicy import ResourcePolicyBase
from core.agility.v2_0.agilitymodel.actions.ResourcePolicy import ResourcePolicyActions

class ResourcePolicy(ResourcePolicyBase, ResourcePolicyActions):
    '''
    classdocs
    '''
    def __init__(self, trace=None, mapping=list(), name=None, apiVersion=None, description=None):
        '''
        Constructor
        @param trace: trace
        @type trace: int
        @param mapping: mapping minOccurs=0 maxOccurs=unbounded
        @type mapping: ResourceMapping
        @param name: name minOccurs=0
        @type name: string
        @param apiVersion: apiVersion minOccurs=0
        @type apiVersion: string
        @param description: description minOccurs=0
        @type description: string
        '''
        ResourcePolicyBase.__init__(self, trace=trace, mapping=mapping, name=name, apiVersion=apiVersion, description=description)
