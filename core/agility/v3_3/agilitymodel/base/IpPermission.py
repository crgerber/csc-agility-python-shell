from core.agility.common.AgilityModelBase import AgilityModelBase

class IpPermissionBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, ipprotocol=None, subgroup=[], cidrblock=[], toport=None, fromport=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'ipProtocol': {'native': True, 'name': 'ipprotocol', 'minOccurs': '0', 'type': 'string'}, 'subgroup': {'maxOccurs': 'unbounded', 'native': False, 'name': 'subgroup', 'minOccurs': '0', 'type': 'Subgroup'}, 'cidrBlock': {'maxOccurs': 'unbounded', 'native': True, 'name': 'cidrblock', 'minOccurs': '0', 'type': 'string'}, 'toPort': {'native': True, 'name': 'toport', 'minOccurs': '0', 'type': 'int'}, 'fromPort': {'native': True, 'name': 'fromport', 'minOccurs': '0', 'type': 'int'}})
        self.ipprotocol = ipprotocol
        self.subgroup = subgroup
        self.cidrblock = cidrblock
        self.toport = toport
        self.fromport = fromport 
