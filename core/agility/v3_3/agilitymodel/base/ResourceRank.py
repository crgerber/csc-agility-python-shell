from core.agility.common.AgilityModelBase import AgilityModelBase

class ResourceRankBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name=None, weight=[], type=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'name': 'name', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'weight': {'name': 'weight', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'ResourceWeight'}, 'type': {'name': 'type', 'native': True, 'type': 'string'}})
        self.name = name
        self.weight = weight
        self.type = type 
