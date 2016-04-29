from core.agility.common.AgilityModelBase import AgilityModelBase

class ApiResponseBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, asset=None, currentrequestindex=None, maxrequests=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'asset': {'native': False, 'name': 'asset', 'minOccurs': '0', 'type': 'Asset'}, 'currentRequestIndex': {'native': True, 'name': 'currentrequestindex', 'type': 'int'}, 'maxRequests': {'native': True, 'name': 'maxrequests', 'type': 'int'}})
        self.asset = asset
        self.currentrequestindex = currentrequestindex
        self.maxrequests = maxrequests 
