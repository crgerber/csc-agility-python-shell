from core.agility.common.AgilityModelBase import AgilityModelBase

class PackageInfoBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name='', version=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'native': True, 'name': 'name', 'type': 'string'}, 'version': {'native': True, 'name': 'version', 'type': 'string'}})
        self.name = name
        self.version = version 
