from core.agility.common.AgilityModelBase import AgilityModelBase

class HotswapListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, hotswapinstances=[], stoppedinstances=[], restartinstances=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'hotswapInstances': {'maxOccurs': 'unbounded', 'native': False, 'name': 'hotswapinstances', 'minOccurs': '0', 'type': 'Link'}, 'stoppedInstances': {'maxOccurs': 'unbounded', 'native': False, 'name': 'stoppedinstances', 'minOccurs': '0', 'type': 'Link'}, 'restartInstances': {'maxOccurs': 'unbounded', 'native': False, 'name': 'restartinstances', 'minOccurs': '0', 'type': 'Link'}})
        self.hotswapinstances = hotswapinstances
        self.stoppedinstances = stoppedinstances
        self.restartinstances = restartinstances 
