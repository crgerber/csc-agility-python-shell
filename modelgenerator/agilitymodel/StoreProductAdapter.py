from base.StoreProductAdapter import StoreProductAdapterBase
from actions.StoreProductAdapter import StoreProductAdapterActions

class StoreProductAdapter(StoreProductAdapterBase, StoreProductAdapterActions):
    '''
    classdocs
    '''
    def __init__(self, url=None, className=None, resource=list(), productType=None):
        '''
        Constructor
        @param url: url minOccurs=0
        @type url: string
        @param className: className minOccurs=0
        @type className: string
        @param resource: resource minOccurs=0 maxOccurs=unbounded
        @type resource: StoreResource
        @param productType: productType minOccurs=0
        @type productType: Link
        '''
        StoreProductAdapterBase.__init__(self, url=url, className=className, resource=resource, productType=productType)
