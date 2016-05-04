from core.agility.common.AgilityModelBase import AgilityModelBase

class ApiInfoBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, realpath=None, version=None, apiname=None, path=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'realPath': {'type': 'string', 'name': 'realpath', 'minOccurs': '0', 'native': True}, 'version': {'type': 'string', 'name': 'version', 'minOccurs': '0', 'native': True}, 'apiName': {'type': 'string', 'name': 'apiname', 'minOccurs': '0', 'native': True}, 'path': {'type': 'string', 'name': 'path', 'minOccurs': '0', 'native': True}})
        self.realpath = realpath
        self.version = version
        self.apiname = apiname
        self.path = path 
