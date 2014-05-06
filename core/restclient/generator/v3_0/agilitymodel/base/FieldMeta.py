from AgilityModelBase import AgilityModelBase

class FieldMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, displayname='', name=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'type': 'string', 'name': 'displayname', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'native': True}})
        self.displayname = displayname
        self.name = name 
