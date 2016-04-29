from core.agility.common.AgilityModelBase import AgilityModelBase

class FieldMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name='', displayname=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'native': True, 'name': 'name', 'type': 'string'}, 'displayName': {'native': True, 'name': 'displayname', 'type': 'string'}})
        self.name = name
        self.displayname = displayname 
