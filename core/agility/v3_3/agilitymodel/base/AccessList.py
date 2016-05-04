from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class AccessListBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, direction=None, protocols=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'direction': {'type': 'AccessListDirection', 'name': 'direction', 'minOccurs': '0', 'native': False}, 'protocols': {'maxOccurs': 'unbounded', 'type': 'Protocol', 'name': 'protocols', 'minOccurs': '0', 'native': False}})
        self.direction = direction
        self.protocols = protocols 
