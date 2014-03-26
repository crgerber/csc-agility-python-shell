from core.agility.common.AgilityModelBase import AgilityModelBase


class FieldMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, displayName='', name=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'type': 'string', 'name': 'displayName', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'native': True}})
        self.displayName = displayName
        self.name = name 
