from .base.PriceEngine import PriceEngineBase
from .actions.PriceEngine import PriceEngineActions

class PriceEngine(PriceEngineBase, PriceEngineActions):
    '''
    classdocs
    '''
    def __init__(self, properties=[]):
        '''
        Constructor
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        '''
        PriceEngineBase.__init__(self, properties=properties)
