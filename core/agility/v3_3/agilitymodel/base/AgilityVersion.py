from core.agility.common.AgilityModelBase import AgilityModelBase

class AgilityVersionBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, build='', url='', version=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'version': {'name': 'version', 'native': True, 'type': 'string'}, 'url': {'name': 'url', 'native': True, 'type': 'string'}, 'build': {'name': 'build', 'native': True, 'type': 'string'}})
        self.build = build
        self.url = url
        self.version = version 
