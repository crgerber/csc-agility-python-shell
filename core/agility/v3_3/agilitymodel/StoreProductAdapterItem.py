from core.agility.v3_3.agilitymodel.base.StoreProductAdapterItem import StoreProductAdapterItemBase
from core.agility.v3_3.agilitymodel.actions.StoreProductAdapterItem import StoreProductAdapterItemActions

class StoreProductAdapterItem(StoreProductAdapterItemBase, StoreProductAdapterItemActions):
    '''
    classdocs
    '''
    def __init__(self, resource=[], description='', link=[], name='', id=None, type=''):
        '''
        Constructor
        @param resource: resource minOccurs=0 maxOccurs=unbounded
        @type resource: StoreResource
        @param description: description
        @type description: string
        @param link: link minOccurs=0 maxOccurs=unbounded
        @type link: Link
        @param name: name
        @type name: string
        @param id: id
        @type id: int
        @param type: type
        @type type: string
        '''
        StoreProductAdapterItemBase.__init__(self, resource=resource, description=description, link=link, name=name, id=id, type=type)
