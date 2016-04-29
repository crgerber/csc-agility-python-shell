from core.agility.v3_3.agilitymodel.base.Resource import ResourceBase
from core.agility.v3_3.agilitymodel.actions.Resource import ResourceActions

class Resource(ResourceBase, ResourceActions):
    '''
    classdocs
    '''
    def __init__(self, quantity=None, editable=None, hostresource=None, resourcetype=None, subtype=None, units=None):
        '''
        Constructor
        @param quantity: quantity
        @type quantity: float
        @param editable: editable minOccurs=0
        @type editable: boolean
        @param hostresource: hostresource minOccurs=0
        @type hostresource: string
        @param resourcetype: resourcetype minOccurs=0
        @type resourcetype: ResourceType
        @param subtype: subtype minOccurs=0
        @type subtype: string
        @param units: units minOccurs=0
        @type units: string
        '''
        ResourceBase.__init__(self, quantity=quantity, editable=editable, hostresource=hostresource, resourcetype=resourcetype, subtype=subtype, units=units)
