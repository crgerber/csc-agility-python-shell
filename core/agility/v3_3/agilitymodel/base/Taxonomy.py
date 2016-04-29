from core.agility.common.AgilityModelBase import AgilityModelBase

class TaxonomyBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, mgmtscriptgroup=None, name='', displayname=None, children=[], id=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'native': True, 'name': 'displayname', 'minOccurs': '0', 'type': 'string'}, 'name': {'native': True, 'name': 'name', 'type': 'string'}, 'mgmtScriptGroup': {'native': False, 'name': 'mgmtscriptgroup', 'minOccurs': '0', 'type': 'Link'}, 'children': {'maxOccurs': 'unbounded', 'native': False, 'name': 'children', 'minOccurs': '0', 'type': 'Taxonomy'}, 'id': {'native': True, 'name': 'id', 'minOccurs': '0', 'type': 'int'}})
        self.mgmtscriptgroup = mgmtscriptgroup
        self.name = name
        self.displayname = displayname
        self.children = children
        self.id = id 
