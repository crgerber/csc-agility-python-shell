from core.agility.common.AgilityModelBase import AgilityModelBase

class ApiResponseBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, currentrequestindex=None, maxrequests=None, asset=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'currentRequestIndex': {'type': 'int', 'name': 'currentrequestindex', 'native': True}, 'maxRequests': {'type': 'int', 'name': 'maxrequests', 'native': True}, 'asset': {'type': 'Asset', 'name': 'asset', 'minOccurs': '0', 'native': False}})
        self.currentrequestindex = currentrequestindex
        self.maxrequests = maxrequests
        self.asset = asset 
