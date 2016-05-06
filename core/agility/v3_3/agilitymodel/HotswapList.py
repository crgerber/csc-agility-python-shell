from core.agility.v3_3.agilitymodel.base.HotswapList import HotswapListBase
from core.agility.v3_3.agilitymodel.actions.HotswapList import HotswapListActions

class HotswapList(HotswapListBase, HotswapListActions):
    '''
    classdocs
    '''
    def __init__(self, restartinstances=[], hotswapinstances=[], stoppedinstances=[]):
        '''
        Constructor
        @param restartinstances: restartinstances minOccurs=0 maxOccurs=unbounded
        @type restartinstances: Link
        @param hotswapinstances: hotswapinstances minOccurs=0 maxOccurs=unbounded
        @type hotswapinstances: Link
        @param stoppedinstances: stoppedinstances minOccurs=0 maxOccurs=unbounded
        @type stoppedinstances: Link
        '''
        HotswapListBase.__init__(self, restartinstances=restartinstances, hotswapinstances=hotswapinstances, stoppedinstances=stoppedinstances)
