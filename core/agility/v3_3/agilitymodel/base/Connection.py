from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class ConnectionBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, destination=None, source=None, variable=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'destination': {'native': False, 'name': 'destination', 'type': 'Link'}, 'source': {'native': False, 'name': 'source', 'type': 'Link'}, 'variable': {'maxOccurs': 'unbounded', 'native': False, 'name': 'variable', 'minOccurs': '0', 'type': 'AssetProperty'}})
        self.destination = destination
        self.source = source
        self.variable = variable 
