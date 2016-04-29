from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class AccessListBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, direction=None, protocols=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'direction': {'native': False, 'name': 'direction', 'minOccurs': '0', 'type': 'AccessListDirection'}, 'protocols': {'maxOccurs': 'unbounded', 'native': False, 'name': 'protocols', 'minOccurs': '0', 'type': 'Protocol'}})
        self.direction = direction
        self.protocols = protocols 
