from core.agility.common.AgilityModelBase import AgilityModelBase

class ApiRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, currentrequestindex=None, maxrequests=None, param=[], cloudid=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'currentRequestIndex': {'type': 'int', 'name': 'currentrequestindex', 'native': True}, 'maxRequests': {'type': 'int', 'name': 'maxrequests', 'native': True}, 'param': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'param', 'minOccurs': '0', 'native': False}, 'cloudId': {'type': 'int', 'name': 'cloudid', 'native': True}})
        self.currentrequestindex = currentrequestindex
        self.maxrequests = maxrequests
        self.param = param
        self.cloudid = cloudid 
