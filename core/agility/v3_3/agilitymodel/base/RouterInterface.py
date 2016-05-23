from core.agility.common.AgilityModelBase import AgilityModelBase

class RouterInterfaceBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, id=None, port=None, subnet=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'id': {'name': 'id', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'port': {'name': 'port', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'subnet': {'name': 'subnet', 'minOccurs': '0', 'native': False, 'type': 'Link'}})
        self.id = id
        self.port = port
        self.subnet = subnet 
