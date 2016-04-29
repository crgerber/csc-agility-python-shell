from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class ContainerRightsBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, user=[], rights=[], projectrole=None, usergroup=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'user': {'maxOccurs': 'unbounded', 'native': False, 'name': 'user', 'minOccurs': '0', 'type': 'Link'}, 'usergroup': {'maxOccurs': 'unbounded', 'native': False, 'name': 'usergroup', 'minOccurs': '0', 'type': 'Link'}, 'projectRole': {'native': False, 'name': 'projectrole', 'minOccurs': '0', 'type': 'Link'}, 'rights': {'maxOccurs': 'unbounded', 'native': False, 'name': 'rights', 'minOccurs': '0', 'type': 'AccessRightSet'}})
        self.user = user
        self.rights = rights
        self.projectrole = projectrole
        self.usergroup = usergroup 
