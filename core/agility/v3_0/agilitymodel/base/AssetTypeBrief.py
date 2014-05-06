from core.agility.common.AgilityModelBase import AgilityModelBase


class AssetTypeBriefBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, entitytype='', displayname='', id=None, jaxbtype='', name=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'entityType': {'type': 'string', 'name': 'entitytype', 'native': True}, 'displayName': {'type': 'string', 'name': 'displayname', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'native': True}, 'jaxbType': {'type': 'string', 'name': 'jaxbtype', 'native': True}})
        self.entitytype = entitytype
        self.displayname = displayname
        self.id = id
        self.jaxbtype = jaxbtype
        self.name = name 
