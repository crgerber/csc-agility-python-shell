from core.agility.v3_3.agilitymodel.base.ApiRequest import ApiRequestBase
from core.agility.v3_3.agilitymodel.actions.ApiRequest import ApiRequestActions

class ApiRequest(ApiRequestBase, ApiRequestActions):
    '''
    classdocs
    '''
    def __init__(self, currentrequestindex=None, cloudid=None, param=[], maxrequests=None):
        '''
        Constructor
        @param currentrequestindex: currentrequestindex
        @type currentrequestindex: int
        @param cloudid: cloudid
        @type cloudid: int
        @param param: param minOccurs=0 maxOccurs=unbounded
        @type param: Property
        @param maxrequests: maxrequests
        @type maxrequests: int
        '''
        ApiRequestBase.__init__(self, currentrequestindex=currentrequestindex, cloudid=cloudid, param=param, maxrequests=maxrequests)
