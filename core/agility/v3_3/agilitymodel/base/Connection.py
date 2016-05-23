from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class ConnectionBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, destination=None, variable=[], source=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'destination': {'name': 'destination', 'native': False, 'type': 'Link'}, 'variable': {'name': 'variable', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetProperty'}, 'source': {'name': 'source', 'native': False, 'type': 'Link'}})
        self.destination = destination
        self.variable = variable
        self.source = source 
