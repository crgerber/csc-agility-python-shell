from core.agility.common.AgilityModelBase import AgilityModelBase

class ResourceMappingBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, description=None, rank=[], condition=None, name=None, exclusion=None, inclusion=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'description': {'name': 'description', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'rank': {'name': 'rank', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'ResourceRank'}, 'condition': {'name': 'condition', 'minOccurs': '0', 'native': False, 'type': 'AssetFilter'}, 'name': {'name': 'name', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'exclusion': {'name': 'exclusion', 'minOccurs': '0', 'native': False, 'type': 'AssetFilter'}, 'inclusion': {'name': 'inclusion', 'minOccurs': '0', 'native': False, 'type': 'AssetFilter'}})
        self.description = description
        self.rank = rank
        self.condition = condition
        self.name = name
        self.exclusion = exclusion
        self.inclusion = inclusion 
