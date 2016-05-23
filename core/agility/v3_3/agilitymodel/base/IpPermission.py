from core.agility.common.AgilityModelBase import AgilityModelBase

class IpPermissionBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, cidrblock=[], ipprotocol=None, subgroup=[], toport=None, fromport=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'fromPort': {'name': 'fromport', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'cidrBlock': {'name': 'cidrblock', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}, 'subgroup': {'name': 'subgroup', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Subgroup'}, 'ipProtocol': {'name': 'ipprotocol', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'toPort': {'name': 'toport', 'minOccurs': '0', 'native': True, 'type': 'int'}})
        self.cidrblock = cidrblock
        self.ipprotocol = ipprotocol
        self.subgroup = subgroup
        self.toport = toport
        self.fromport = fromport 
