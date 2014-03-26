from core.agility.v3_0.agilitymodel.base.HotswapList import HotswapListBase
from core.agility.v3_0.agilitymodel.actions.HotswapList import HotswapListActions

class HotswapList(HotswapListBase, HotswapListActions):
    '''
    classdocs
    '''
    def __init__(self, restartinstances=[], hotswapinstances=[]):
        '''
        Constructor
        @param restartinstances: restartinstances minOccurs=0 maxOccurs=unbounded
        @type restartinstances: Link
        @param hotswapinstances: hotswapinstances minOccurs=0 maxOccurs=unbounded
        @type hotswapinstances: Link
        '''
        HotswapListBase.__init__(self, restartinstances=restartinstances, hotswapinstances=hotswapinstances)
