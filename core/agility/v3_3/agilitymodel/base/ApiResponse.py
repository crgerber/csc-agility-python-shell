from core.agility.common.AgilityModelBase import AgilityModelBase

class ApiResponseBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, asset=None, currentrequestindex=None, maxrequests=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'asset': {'name': 'asset', 'minOccurs': '0', 'native': False, 'type': 'Asset'}, 'currentRequestIndex': {'name': 'currentrequestindex', 'native': True, 'type': 'int'}, 'maxRequests': {'name': 'maxrequests', 'native': True, 'type': 'int'}})
        self.asset = asset
        self.currentrequestindex = currentrequestindex
        self.maxrequests = maxrequests 
