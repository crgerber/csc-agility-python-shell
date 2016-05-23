from core.agility.common.AgilityModelBase import AgilityModelBase

class AliasListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, alias=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'alias': {'name': 'alias', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Alias'}})
        self.alias = alias 
