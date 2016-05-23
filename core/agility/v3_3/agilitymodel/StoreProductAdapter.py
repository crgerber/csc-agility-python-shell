from core.agility.v3_3.agilitymodel.base.StoreProductAdapter import StoreProductAdapterBase
from core.agility.v3_3.agilitymodel.actions.StoreProductAdapter import StoreProductAdapterActions

class StoreProductAdapter(StoreProductAdapterBase, StoreProductAdapterActions):
    '''
    classdocs
    '''
    def __init__(self, resource=[], url=None, producttype=None, classname=None):
        '''
        Constructor
        @param resource: resource minOccurs=0 maxOccurs=unbounded
        @type resource: StoreResource
        @param url: url minOccurs=0
        @type url: string
        @param producttype: producttype minOccurs=0
        @type producttype: Link
        @param classname: classname minOccurs=0
        @type classname: string
        '''
        StoreProductAdapterBase.__init__(self, resource=resource, url=url, producttype=producttype, classname=classname)
