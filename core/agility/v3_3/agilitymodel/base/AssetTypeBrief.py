from core.agility.common.AgilityModelBase import AgilityModelBase

class AssetTypeBriefBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, path='', name='', displayname='', entitytype='', jaxbtype='', id=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'name': 'name', 'native': True, 'type': 'string'}, 'displayName': {'name': 'displayname', 'native': True, 'type': 'string'}, 'entityType': {'name': 'entitytype', 'native': True, 'type': 'string'}, 'jaxbType': {'name': 'jaxbtype', 'native': True, 'type': 'string'}, 'path': {'name': 'path', 'native': True, 'type': 'string'}, 'id': {'name': 'id', 'native': True, 'type': 'int'}})
        self.path = path
        self.name = name
        self.displayname = displayname
        self.entitytype = entitytype
        self.jaxbtype = jaxbtype
        self.id = id 
