from core.agility.common.AgilityModelBase import AgilityModelBase

class PackageInfoBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, version='', name=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'version': {'type': 'string', 'name': 'version', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'native': True}})
        self.version = version
        self.name = name 
