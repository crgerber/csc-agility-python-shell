from core.agility.common.AgilityModelBase import AgilityModelBase

class ResourceRankBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, weight=[], name=None, type=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'weight': {'maxOccurs': 'unbounded', 'native': False, 'name': 'weight', 'minOccurs': '0', 'type': 'ResourceWeight'}, 'name': {'native': True, 'name': 'name', 'minOccurs': '0', 'type': 'string'}, 'type': {'native': True, 'name': 'type', 'type': 'string'}})
        self.weight = weight
        self.name = name
        self.type = type 
