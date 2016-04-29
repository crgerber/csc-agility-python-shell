from core.agility.common.AgilityModelBase import AgilityModelBase

class AgilityVersionBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, build='', version='', url=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'build': {'native': True, 'name': 'build', 'type': 'string'}, 'version': {'native': True, 'name': 'version', 'type': 'string'}, 'url': {'native': True, 'name': 'url', 'type': 'string'}})
        self.build = build
        self.version = version
        self.url = url 
