from core.agility.v2_0.agilitymodel.base.PriceEngine import PriceEngineBase
from core.agility.v2_0.agilitymodel.actions.PriceEngine import PriceEngineActions

class PriceEngine(PriceEngineBase, PriceEngineActions):
    '''
    classdocs
    '''
    def __init__(self, properties=list()):
        '''
        Constructor
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        '''
        PriceEngineBase.__init__(self, properties=properties)
