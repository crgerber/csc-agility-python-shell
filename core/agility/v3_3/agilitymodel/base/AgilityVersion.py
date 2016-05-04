from core.agility.common.AgilityModelBase import AgilityModelBase

class AgilityVersionBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, url='', version='', build=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'url': {'type': 'string', 'name': 'url', 'native': True}, 'version': {'type': 'string', 'name': 'version', 'native': True}, 'build': {'type': 'string', 'name': 'build', 'native': True}})
        self.url = url
        self.version = version
        self.build = build 
