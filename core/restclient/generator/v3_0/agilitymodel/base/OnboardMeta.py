from AgilityModelBase import AgilityModelBase

class OnboardMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, type='', supportedinstancefield=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'type': {'type': 'string', 'name': 'type', 'native': True}, 'supportedInstanceField': {'maxOccurs': 'unbounded', 'type': 'FieldMeta', 'name': 'supportedinstancefield', 'minOccurs': '0', 'native': False}})
        self.type = type
        self.supportedinstancefield = supportedinstancefield 
