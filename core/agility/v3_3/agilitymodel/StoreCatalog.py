from core.agility.v3_3.agilitymodel.base.StoreCatalog import StoreCatalogBase
from core.agility.v3_3.agilitymodel.actions.StoreCatalog import StoreCatalogActions

class StoreCatalog(StoreCatalogBase, StoreCatalogActions):
    '''
    classdocs
    '''
    def __init__(self, products=[]):
        '''
        Constructor
        @param products: products minOccurs=0 maxOccurs=unbounded
        @type products: Link
        '''
        StoreCatalogBase.__init__(self, products=products)
