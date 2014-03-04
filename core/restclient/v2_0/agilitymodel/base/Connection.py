from core.restclient.v2_0.agilitymodel.base.Item import ItemBase

class ConnectionBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, variable=list(), source=None, destination=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'variable': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'variable', 'minOccurs': '0', 'native': False}, 'source': {'type': 'Link', 'name': 'source', 'native': False}, 'destination': {'type': 'Link', 'name': 'destination', 'native': False}})
        self.variable = variable
        self.source = source
        self.destination = destination 
