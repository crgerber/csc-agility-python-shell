from core.agility.common.AgilityModelBase import AgilityModelBase

class ResourceRankBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, type='', name=None, weight=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'type': {'type': 'string', 'name': 'type', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'minOccurs': '0', 'native': True}, 'weight': {'maxOccurs': 'unbounded', 'type': 'ResourceWeight', 'name': 'weight', 'minOccurs': '0', 'native': False}})
        self.type = type
        self.name = name
        self.weight = weight 
