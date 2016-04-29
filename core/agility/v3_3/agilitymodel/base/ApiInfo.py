from core.agility.common.AgilityModelBase import AgilityModelBase

class ApiInfoBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, path=None, realpath=None, version=None, apiname=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'realPath': {'native': True, 'name': 'realpath', 'minOccurs': '0', 'type': 'string'}, 'path': {'native': True, 'name': 'path', 'minOccurs': '0', 'type': 'string'}, 'apiName': {'native': True, 'name': 'apiname', 'minOccurs': '0', 'type': 'string'}, 'version': {'native': True, 'name': 'version', 'minOccurs': '0', 'type': 'string'}})
        self.path = path
        self.realpath = realpath
        self.version = version
        self.apiname = apiname 
