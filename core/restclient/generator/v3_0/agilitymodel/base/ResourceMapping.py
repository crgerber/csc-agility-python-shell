from AgilityModelBase import AgilityModelBase

class ResourceMappingBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, exclusion=None, inclusion=None, description=None, rank=[], condition=None, name=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'type': 'string', 'name': 'name', 'minOccurs': '0', 'native': True}, 'inclusion': {'type': 'AssetFilter', 'name': 'inclusion', 'minOccurs': '0', 'native': False}, 'exclusion': {'type': 'AssetFilter', 'name': 'exclusion', 'minOccurs': '0', 'native': False}, 'rank': {'maxOccurs': 'unbounded', 'type': 'ResourceRank', 'name': 'rank', 'minOccurs': '0', 'native': False}, 'condition': {'type': 'AssetFilter', 'name': 'condition', 'minOccurs': '0', 'native': False}, 'description': {'type': 'string', 'name': 'description', 'minOccurs': '0', 'native': True}})
        self.exclusion = exclusion
        self.inclusion = inclusion
        self.description = description
        self.rank = rank
        self.condition = condition
        self.name = name 
