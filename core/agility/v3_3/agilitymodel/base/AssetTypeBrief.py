from core.agility.common.AgilityModelBase import AgilityModelBase

class AssetTypeBriefBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, entitytype='', path='', name='', displayname='', jaxbtype='', id=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'entityType': {'native': True, 'name': 'entitytype', 'type': 'string'}, 'path': {'native': True, 'name': 'path', 'type': 'string'}, 'name': {'native': True, 'name': 'name', 'type': 'string'}, 'displayName': {'native': True, 'name': 'displayname', 'type': 'string'}, 'jaxbType': {'native': True, 'name': 'jaxbtype', 'type': 'string'}, 'id': {'native': True, 'name': 'id', 'type': 'int'}})
        self.entitytype = entitytype
        self.path = path
        self.name = name
        self.displayname = displayname
        self.jaxbtype = jaxbtype
        self.id = id 
