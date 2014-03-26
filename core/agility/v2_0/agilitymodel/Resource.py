from core.agility.v2_0.agilitymodel.base.Resource import ResourceBase
from core.agility.v2_0.agilitymodel.actions.Resource import ResourceActions

class Resource(ResourceBase, ResourceActions):
    '''
    classdocs
    '''
    def __init__(self, resourceType=None, editable=None, subType=None, hostResource=None, units=None, quantity=None):
        '''
        Constructor
        @param resourceType: resourceType minOccurs=0
        @type resourceType: ResourceType
        @param editable: editable minOccurs=0
        @type editable: boolean
        @param subType: subType minOccurs=0
        @type subType: string
        @param hostResource: hostResource minOccurs=0
        @type hostResource: string
        @param units: units minOccurs=0
        @type units: string
        @param quantity: quantity
        @type quantity: float
        '''
        ResourceBase.__init__(self, resourceType=resourceType, editable=editable, subType=subType, hostResource=hostResource, units=units, quantity=quantity)
