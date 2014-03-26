from AgilityModelBase import AgilityModelBase

class PolicyMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, type=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'type': {'type': 'string', 'name': 'type', 'native': True}})
        self.type = type 
