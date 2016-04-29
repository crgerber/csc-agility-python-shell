from .base.Resource import ResourceBase
from .actions.Resource import ResourceActions

class Resource(ResourceBase, ResourceActions):
    '''
    classdocs
    '''
    def __init__(self, resourcetype=None, editable=None, subtype=None, hostresource=None, units=None, quantity=None):
        '''
        Constructor
        @param resourcetype: resourcetype minOccurs=0
        @type resourcetype: ResourceType
        @param editable: editable minOccurs=0
        @type editable: boolean
        @param subtype: subtype minOccurs=0
        @type subtype: string
        @param hostresource: hostresource minOccurs=0
        @type hostresource: string
        @param units: units minOccurs=0
        @type units: string
        @param quantity: quantity
        @type quantity: float
        '''
        ResourceBase.__init__(self, resourcetype=resourcetype, editable=editable, subtype=subtype, hostresource=hostresource, units=units, quantity=quantity)
