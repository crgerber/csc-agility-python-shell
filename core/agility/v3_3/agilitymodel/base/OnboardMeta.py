from core.agility.common.AgilityModelBase import AgilityModelBase

class OnboardMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, supportedinstancefield=[], type=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'supportedInstanceField': {'maxOccurs': 'unbounded', 'native': False, 'name': 'supportedinstancefield', 'minOccurs': '0', 'type': 'FieldMeta'}, 'type': {'native': True, 'name': 'type', 'type': 'string'}})
        self.supportedinstancefield = supportedinstancefield
        self.type = type 
