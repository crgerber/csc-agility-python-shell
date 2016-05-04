from core.agility.common.AgilityModelBase import AgilityModelBase

class HotswapListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, restartinstances=[], hotswapinstances=[], stoppedinstances=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'restartInstances': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'restartinstances', 'minOccurs': '0', 'native': False}, 'hotswapInstances': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'hotswapinstances', 'minOccurs': '0', 'native': False}, 'stoppedInstances': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'stoppedinstances', 'minOccurs': '0', 'native': False}})
        self.restartinstances = restartinstances
        self.hotswapinstances = hotswapinstances
        self.stoppedinstances = stoppedinstances 
