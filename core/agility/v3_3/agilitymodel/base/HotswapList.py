from core.agility.common.AgilityModelBase import AgilityModelBase

class HotswapListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, stoppedinstances=[], hotswapinstances=[], restartinstances=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'stoppedInstances': {'name': 'stoppedinstances', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'hotswapInstances': {'name': 'hotswapinstances', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'restartInstances': {'name': 'restartinstances', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.stoppedinstances = stoppedinstances
        self.hotswapinstances = hotswapinstances
        self.restartinstances = restartinstances 
