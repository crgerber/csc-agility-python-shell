from Item import ItemBase

class ContainerRightsBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, projectrole=None, rights=[], user=[], usergroup=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'projectRole': {'type': 'Link', 'name': 'projectrole', 'minOccurs': '0', 'native': False}, 'usergroup': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'usergroup', 'minOccurs': '0', 'native': False}, 'user': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'user', 'minOccurs': '0', 'native': False}, 'rights': {'maxOccurs': 'unbounded', 'type': 'AccessRightSet', 'name': 'rights', 'minOccurs': '0', 'native': False}})
        self.projectrole = projectrole
        self.rights = rights
        self.user = user
        self.usergroup = usergroup 
