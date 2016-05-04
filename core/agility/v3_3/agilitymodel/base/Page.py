from Asset import AssetBase

class PageBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, selection=[], layout=None, users=[], title='', usergroups=[], context=None, menucategory=''):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'userGroups': {'maxOccurs': 'unbounded', 'type': 'int', 'name': 'usergroups', 'minOccurs': '0', 'native': True}, 'layout': {'type': 'PageLayout', 'name': 'layout', 'native': False}, 'users': {'maxOccurs': 'unbounded', 'type': 'int', 'name': 'users', 'minOccurs': '0', 'native': True}, 'title': {'type': 'string', 'name': 'title', 'native': True}, 'selection': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'selection', 'minOccurs': '0', 'native': False}, 'context': {'type': 'PageContext', 'name': 'context', 'native': False}, 'menuCategory': {'type': 'string', 'name': 'menucategory', 'native': True}})
        self.selection = selection
        self.layout = layout
        self.users = users
        self.title = title
        self.usergroups = usergroups
        self.context = context
        self.menucategory = menucategory 
