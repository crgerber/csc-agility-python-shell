from AgilityModelBase import AgilityModelBase

class TaxonomyBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, mgmtscriptgroup=None, children=[], displayname=None, id=None, name=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'type': 'string', 'name': 'displayname', 'minOccurs': '0', 'native': True}, 'mgmtScriptGroup': {'type': 'Link', 'name': 'mgmtscriptgroup', 'minOccurs': '0', 'native': False}, 'children': {'maxOccurs': 'unbounded', 'type': 'Taxonomy', 'name': 'children', 'minOccurs': '0', 'native': False}, 'name': {'type': 'string', 'name': 'name', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'minOccurs': '0', 'native': True}})
        self.mgmtscriptgroup = mgmtscriptgroup
        self.children = children
        self.displayname = displayname
        self.id = id
        self.name = name 
