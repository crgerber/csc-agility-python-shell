from core.agility.common.AgilityModelBase import AgilityModelBase

class IpPermissionBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, toport=None, ipprotocol=None, subgroup=[], cidrblock=[], fromport=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'toPort': {'type': 'int', 'name': 'toport', 'minOccurs': '0', 'native': True}, 'ipProtocol': {'type': 'string', 'name': 'ipprotocol', 'minOccurs': '0', 'native': True}, 'cidrBlock': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'cidrblock', 'minOccurs': '0', 'native': True}, 'fromPort': {'type': 'int', 'name': 'fromport', 'minOccurs': '0', 'native': True}, 'subgroup': {'maxOccurs': 'unbounded', 'type': 'Subgroup', 'name': 'subgroup', 'minOccurs': '0', 'native': False}})
        self.toport = toport
        self.ipprotocol = ipprotocol
        self.subgroup = subgroup
        self.cidrblock = cidrblock
        self.fromport = fromport 
