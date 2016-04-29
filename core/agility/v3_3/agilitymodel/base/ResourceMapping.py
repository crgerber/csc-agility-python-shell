from core.agility.common.AgilityModelBase import AgilityModelBase

class ResourceMappingBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, condition=None, exclusion=None, description=None, name=None, rank=[], inclusion=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'exclusion': {'native': False, 'name': 'exclusion', 'minOccurs': '0', 'type': 'AssetFilter'}, 'description': {'native': True, 'name': 'description', 'minOccurs': '0', 'type': 'string'}, 'name': {'native': True, 'name': 'name', 'minOccurs': '0', 'type': 'string'}, 'condition': {'native': False, 'name': 'condition', 'minOccurs': '0', 'type': 'AssetFilter'}, 'rank': {'maxOccurs': 'unbounded', 'native': False, 'name': 'rank', 'minOccurs': '0', 'type': 'ResourceRank'}, 'inclusion': {'native': False, 'name': 'inclusion', 'minOccurs': '0', 'type': 'AssetFilter'}})
        self.condition = condition
        self.exclusion = exclusion
        self.description = description
        self.name = name
        self.rank = rank
        self.inclusion = inclusion 
