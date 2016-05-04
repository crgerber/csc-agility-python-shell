from core.agility.common.AgilityModelBase import AgilityModelBase

class FixedIPBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, subnet=None, ipaddress=None, id=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'subnet': {'type': 'Link', 'name': 'subnet', 'minOccurs': '0', 'native': False}, 'ipAddress': {'type': 'string', 'name': 'ipaddress', 'minOccurs': '0', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'minOccurs': '0', 'native': True}})
        self.subnet = subnet
        self.ipaddress = ipaddress
        self.id = id 
