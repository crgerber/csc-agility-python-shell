from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class PageBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, menucategory='', context=None, users=[], title='', selection=[], usergroups=[], layout=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'menuCategory': {'native': True, 'name': 'menucategory', 'type': 'string'}, 'context': {'native': False, 'name': 'context', 'type': 'PageContext'}, 'users': {'maxOccurs': 'unbounded', 'native': True, 'name': 'users', 'minOccurs': '0', 'type': 'int'}, 'title': {'native': True, 'name': 'title', 'type': 'string'}, 'selection': {'maxOccurs': 'unbounded', 'native': False, 'name': 'selection', 'minOccurs': '0', 'type': 'AssetProperty'}, 'userGroups': {'maxOccurs': 'unbounded', 'native': True, 'name': 'usergroups', 'minOccurs': '0', 'type': 'int'}, 'layout': {'native': False, 'name': 'layout', 'type': 'PageLayout'}})
        self.menucategory = menucategory
        self.context = context
        self.users = users
        self.title = title
        self.selection = selection
        self.usergroups = usergroups
        self.layout = layout 
