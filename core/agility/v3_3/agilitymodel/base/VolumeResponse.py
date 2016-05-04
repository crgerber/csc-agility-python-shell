from core.agility.common.AgilityModelBase import AgilityModelBase

class VolumeResponseBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, errormessage=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'errorMessage': {'type': 'string', 'name': 'errormessage', 'minOccurs': '0', 'native': True}})
        self.errormessage = errormessage 
