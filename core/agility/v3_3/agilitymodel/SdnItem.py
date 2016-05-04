from core.agility.v3_3.agilitymodel.base.SdnItem import SdnItemBase
from core.agility.v3_3.agilitymodel.actions.SdnItem import SdnItemActions

class SdnItem(SdnItemBase, SdnItemActions):
    '''
    classdocs
    '''
    def __init__(self, state=None, properties=[]):
        '''
        Constructor
        @param state: state minOccurs=0
        @type state: SdnState
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        '''
        SdnItemBase.__init__(self, state=state, properties=properties)
