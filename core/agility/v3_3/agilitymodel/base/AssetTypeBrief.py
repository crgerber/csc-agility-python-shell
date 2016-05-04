from core.agility.common.AgilityModelBase import AgilityModelBase

class AssetTypeBriefBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, displayname='', name='', entitytype='', jaxbtype='', path='', id=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'type': 'string', 'name': 'displayname', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'native': True}, 'entityType': {'type': 'string', 'name': 'entitytype', 'native': True}, 'jaxbType': {'type': 'string', 'name': 'jaxbtype', 'native': True}, 'path': {'type': 'string', 'name': 'path', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'native': True}})
        self.displayname = displayname
        self.name = name
        self.entitytype = entitytype
        self.jaxbtype = jaxbtype
        self.path = path
        self.id = id 
