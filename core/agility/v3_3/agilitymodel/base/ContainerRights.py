from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class ContainerRightsBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, rights=[], projectrole=None, usergroup=[], user=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'rights': {'name': 'rights', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AccessRightSet'}, 'projectRole': {'name': 'projectrole', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'usergroup': {'name': 'usergroup', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'user': {'name': 'user', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.rights = rights
        self.projectrole = projectrole
        self.usergroup = usergroup
        self.user = user 
