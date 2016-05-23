from core.agility.v3_3.agilitymodel.base.Resource import ResourceBase
from core.agility.v3_3.agilitymodel.actions.Resource import ResourceActions

class Resource(ResourceBase, ResourceActions):
    '''
    classdocs
    '''
    def __init__(self, editable=None, quantity=None, units=None, hostresource=None, resourcetype=None, subtype=None):
        '''
        Constructor
        @param editable: editable minOccurs=0
        @type editable: boolean
        @param quantity: quantity
        @type quantity: float
        @param units: units minOccurs=0
        @type units: string
        @param hostresource: hostresource minOccurs=0
        @type hostresource: string
        @param resourcetype: resourcetype minOccurs=0
        @type resourcetype: ResourceType
        @param subtype: subtype minOccurs=0
        @type subtype: string
        '''
        ResourceBase.__init__(self, editable=editable, quantity=quantity, units=units, hostresource=hostresource, resourcetype=resourcetype, subtype=subtype)
