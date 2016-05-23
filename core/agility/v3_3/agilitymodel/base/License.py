from core.agility.common.AgilityModelBase import AgilityModelBase

class LicenseBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, license=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'license': {'name': 'license', 'native': True, 'type': 'string'}})
        self.license = license 
