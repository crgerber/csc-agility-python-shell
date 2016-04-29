from .Asset import AssetBase

class MgmtScriptGroupBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, operatingsystem=None, mgmtscripts=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'operatingSystem': {'type': 'string', 'name': 'operatingsystem', 'minOccurs': '0', 'native': True}, 'mgmtScripts': {'maxOccurs': 'unbounded', 'type': 'MgmtScript', 'name': 'mgmtscripts', 'minOccurs': '0', 'native': False}})
        self.operatingsystem = operatingsystem
        self.mgmtscripts = mgmtscripts 
