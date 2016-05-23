from core.agility.common.AgilityModelBase import AgilityModelBase

class FieldMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name='', displayname=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'name': 'name', 'native': True, 'type': 'string'}, 'displayName': {'name': 'displayname', 'native': True, 'type': 'string'}})
        self.name = name
        self.displayname = displayname 
