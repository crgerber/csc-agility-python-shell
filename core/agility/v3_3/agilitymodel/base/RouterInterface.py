from core.agility.common.AgilityModelBase import AgilityModelBase

class RouterInterfaceBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, subnet=None, id=None, port=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'subnet': {'type': 'Link', 'name': 'subnet', 'minOccurs': '0', 'native': False}, 'id': {'type': 'int', 'name': 'id', 'minOccurs': '0', 'native': True}, 'port': {'type': 'Link', 'name': 'port', 'minOccurs': '0', 'native': False}})
        self.subnet = subnet
        self.id = id
        self.port = port 
