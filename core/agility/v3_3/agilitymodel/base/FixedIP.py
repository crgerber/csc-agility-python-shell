from core.agility.common.AgilityModelBase import AgilityModelBase

class FixedIPBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, id=None, subnet=None, ipaddress=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'id': {'name': 'id', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'subnet': {'name': 'subnet', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'ipAddress': {'name': 'ipaddress', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.id = id
        self.subnet = subnet
        self.ipaddress = ipaddress 
