from core.agility.common.AgilityModelBase import AgilityModelBase

class ApiInfoBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, realpath=None, path=None, apiname=None, version=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'realPath': {'name': 'realpath', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'path': {'name': 'path', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'apiName': {'name': 'apiname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'version': {'name': 'version', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.realpath = realpath
        self.path = path
        self.apiname = apiname
        self.version = version 
