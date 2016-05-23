from core.agility.v3_3.agilitymodel.base.HotswapList import HotswapListBase
from core.agility.v3_3.agilitymodel.actions.HotswapList import HotswapListActions

class HotswapList(HotswapListBase, HotswapListActions):
    '''
    classdocs
    '''
    def __init__(self, stoppedinstances=[], hotswapinstances=[], restartinstances=[]):
        '''
        Constructor
        @param stoppedinstances: stoppedinstances minOccurs=0 maxOccurs=unbounded
        @type stoppedinstances: Link
        @param hotswapinstances: hotswapinstances minOccurs=0 maxOccurs=unbounded
        @type hotswapinstances: Link
        @param restartinstances: restartinstances minOccurs=0 maxOccurs=unbounded
        @type restartinstances: Link
        '''
        HotswapListBase.__init__(self, stoppedinstances=stoppedinstances, hotswapinstances=hotswapinstances, restartinstances=restartinstances)
