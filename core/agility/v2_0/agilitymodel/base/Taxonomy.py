from core.agility.common.AgilityModelBase import AgilityModelBase


class TaxonomyBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, children=list(), displayName=None, id=None, name=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'type': 'string', 'name': 'displayName', 'minOccurs': '0', 'native': True}, 'children': {'maxOccurs': 'unbounded', 'type': 'Taxonomy', 'name': 'children', 'minOccurs': '0', 'native': False}, 'name': {'type': 'string', 'name': 'name', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'minOccurs': '0', 'native': True}})
        self.children = children
        self.displayName = displayName
        self.id = id
        self.name = name 
