from core.agility.common.AgilityModelBase import AgilityModelBase

class FixedIPBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, ipaddress=None, subnet=None, id=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'ipAddress': {'native': True, 'name': 'ipaddress', 'minOccurs': '0', 'type': 'string'}, 'subnet': {'native': False, 'name': 'subnet', 'minOccurs': '0', 'type': 'Link'}, 'id': {'native': True, 'name': 'id', 'minOccurs': '0', 'type': 'int'}})
        self.ipaddress = ipaddress
        self.subnet = subnet
        self.id = id 
