from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class PageBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, title='', context=None, selection=[], menucategory='', usergroups=[], layout=None, users=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'title': {'name': 'title', 'native': True, 'type': 'string'}, 'context': {'name': 'context', 'native': False, 'type': 'PageContext'}, 'selection': {'name': 'selection', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetProperty'}, 'menuCategory': {'name': 'menucategory', 'native': True, 'type': 'string'}, 'userGroups': {'name': 'usergroups', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'int'}, 'layout': {'name': 'layout', 'native': False, 'type': 'PageLayout'}, 'users': {'name': 'users', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'int'}})
        self.title = title
        self.context = context
        self.selection = selection
        self.menucategory = menucategory
        self.usergroups = usergroups
        self.layout = layout
        self.users = users 
