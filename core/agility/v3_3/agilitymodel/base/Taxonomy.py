from core.agility.common.AgilityModelBase import AgilityModelBase

class TaxonomyBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, id=None, name='', displayname=None, children=[], mgmtscriptgroup=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'id': {'name': 'id', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'name': {'name': 'name', 'native': True, 'type': 'string'}, 'displayName': {'name': 'displayname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'children': {'name': 'children', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Taxonomy'}, 'mgmtScriptGroup': {'name': 'mgmtscriptgroup', 'minOccurs': '0', 'native': False, 'type': 'Link'}})
        self.id = id
        self.name = name
        self.displayname = displayname
        self.children = children
        self.mgmtscriptgroup = mgmtscriptgroup 
