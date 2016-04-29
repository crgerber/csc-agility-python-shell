from core.agility.common.AgilityModelBase import AgilityModelBase

class RouterInterfaceBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, subnet=None, id=None, port=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'subnet': {'native': False, 'name': 'subnet', 'minOccurs': '0', 'type': 'Link'}, 'id': {'native': True, 'name': 'id', 'minOccurs': '0', 'type': 'int'}, 'port': {'native': False, 'name': 'port', 'minOccurs': '0', 'type': 'Link'}})
        self.subnet = subnet
        self.id = id
        self.port = port 
