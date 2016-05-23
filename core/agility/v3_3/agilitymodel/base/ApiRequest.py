from core.agility.common.AgilityModelBase import AgilityModelBase

class ApiRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, currentrequestindex=None, cloudid=None, param=[], maxrequests=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'currentRequestIndex': {'name': 'currentrequestindex', 'native': True, 'type': 'int'}, 'cloudId': {'name': 'cloudid', 'native': True, 'type': 'int'}, 'param': {'name': 'param', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Property'}, 'maxRequests': {'name': 'maxrequests', 'native': True, 'type': 'int'}})
        self.currentrequestindex = currentrequestindex
        self.cloudid = cloudid
        self.param = param
        self.maxrequests = maxrequests 
