from base.StoreProductAdapter import StoreProductAdapterBase
from actions.StoreProductAdapter import StoreProductAdapterActions

class StoreProductAdapter(StoreProductAdapterBase, StoreProductAdapterActions):
    '''
    classdocs
    '''
    def __init__(self, url=None, classname=None, resource=[], producttype=None):
        '''
        Constructor
        @param url: url minOccurs=0
        @type url: string
        @param classname: classname minOccurs=0
        @type classname: string
        @param resource: resource minOccurs=0 maxOccurs=unbounded
        @type resource: StoreResource
        @param producttype: producttype minOccurs=0
        @type producttype: Link
        '''
        StoreProductAdapterBase.__init__(self, url=url, classname=classname, resource=resource, producttype=producttype)
