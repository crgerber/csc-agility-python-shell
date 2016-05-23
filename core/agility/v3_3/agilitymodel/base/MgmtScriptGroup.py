from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class MgmtScriptGroupBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, operatingsystem=None, mgmtscripts=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'operatingSystem': {'name': 'operatingsystem', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'mgmtScripts': {'name': 'mgmtscripts', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'MgmtScript'}})
        self.operatingsystem = operatingsystem
        self.mgmtscripts = mgmtscripts 
