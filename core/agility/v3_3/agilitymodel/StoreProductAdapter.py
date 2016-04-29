from core.agility.v3_3.agilitymodel.base.StoreProductAdapter import StoreProductAdapterBase
from core.agility.v3_3.agilitymodel.actions.StoreProductAdapter import StoreProductAdapterActions

class StoreProductAdapter(StoreProductAdapterBase, StoreProductAdapterActions):
    '''
    classdocs
    '''
    def __init__(self, producttype=None, classname=None, url=None, resource=[]):
        '''
        Constructor
        @param producttype: producttype minOccurs=0
        @type producttype: Link
        @param classname: classname minOccurs=0
        @type classname: string
        @param url: url minOccurs=0
        @type url: string
        @param resource: resource minOccurs=0 maxOccurs=unbounded
        @type resource: StoreResource
        '''
        StoreProductAdapterBase.__init__(self, producttype=producttype, classname=classname, url=url, resource=resource)
