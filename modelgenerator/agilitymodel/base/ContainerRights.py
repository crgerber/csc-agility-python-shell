from Item import ItemBase

class ContainerRightsBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, projectRole=None, rights=list(), user=list(), usergroup=list()):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'projectRole': {'type': 'Link', 'name': 'projectRole', 'minOccurs': '0', 'native': False}, 'usergroup': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'usergroup', 'minOccurs': '0', 'native': False}, 'user': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'user', 'minOccurs': '0', 'native': False}, 'rights': {'maxOccurs': 'unbounded', 'type': 'AccessRightSet', 'name': 'rights', 'minOccurs': '0', 'native': False}})
        self.projectRole = projectRole
        self.rights = rights
        self.user = user
        self.usergroup = usergroup 
