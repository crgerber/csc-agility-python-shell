from core.agility.common.AgilityModelBase import AgilityModelBase


class AssetTypeBriefBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, entityType='', displayName='', id=None, jaxbType='', name=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'entityType': {'type': 'string', 'name': 'entityType', 'native': True}, 'displayName': {'type': 'string', 'name': 'displayName', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'native': True}, 'jaxbType': {'type': 'string', 'name': 'jaxbType', 'native': True}})
        self.entityType = entityType
        self.displayName = displayName
        self.id = id
        self.jaxbType = jaxbType
        self.name = name 
