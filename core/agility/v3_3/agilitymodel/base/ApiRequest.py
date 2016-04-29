from core.agility.common.AgilityModelBase import AgilityModelBase

class ApiRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, maxrequests=None, cloudid=None, currentrequestindex=None, param=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'cloudId': {'native': True, 'name': 'cloudid', 'type': 'int'}, 'param': {'maxOccurs': 'unbounded', 'native': False, 'name': 'param', 'minOccurs': '0', 'type': 'Property'}, 'currentRequestIndex': {'native': True, 'name': 'currentrequestindex', 'type': 'int'}, 'maxRequests': {'native': True, 'name': 'maxrequests', 'type': 'int'}})
        self.maxrequests = maxrequests
        self.cloudid = cloudid
        self.currentrequestindex = currentrequestindex
        self.param = param 
