from core.agility.common.AgilityModelBase import AgilityModelBase

class VolumeResponseBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, errormessage=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'errorMessage': {'name': 'errormessage', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.errormessage = errormessage 
