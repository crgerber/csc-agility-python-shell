from core.agility.v3_3.agilitymodel.base.StoreProductAdapterItem import StoreProductAdapterItemBase
from core.agility.v3_3.agilitymodel.actions.StoreProductAdapterItem import StoreProductAdapterItemActions

class StoreProductAdapterItem(StoreProductAdapterItemBase, StoreProductAdapterItemActions):
    '''
    classdocs
    '''
    def __init__(self, name='', description='', id=None, link=[], type='', resource=[]):
        '''
        Constructor
        @param name: name
        @type name: string
        @param description: description
        @type description: string
        @param id: id
        @type id: int
        @param link: link minOccurs=0 maxOccurs=unbounded
        @type link: Link
        @param type: type
        @type type: string
        @param resource: resource minOccurs=0 maxOccurs=unbounded
        @type resource: StoreResource
        '''
        StoreProductAdapterItemBase.__init__(self, name=name, description=description, id=id, link=link, type=type, resource=resource)
