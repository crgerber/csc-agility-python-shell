from core.agility.common.AgilityModelBase import AgilityModelBase

class PackageInfoBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name='', version=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'name': 'name', 'native': True, 'type': 'string'}, 'version': {'name': 'version', 'native': True, 'type': 'string'}})
        self.name = name
        self.version = version 
