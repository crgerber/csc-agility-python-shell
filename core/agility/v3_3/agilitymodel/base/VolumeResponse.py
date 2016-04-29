from core.agility.common.AgilityModelBase import AgilityModelBase

class VolumeResponseBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, errormessage=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'errorMessage': {'native': True, 'name': 'errormessage', 'minOccurs': '0', 'type': 'string'}})
        self.errormessage = errormessage 
