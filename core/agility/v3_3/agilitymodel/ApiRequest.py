from base.ApiRequest import ApiRequestBase
from actions.ApiRequest import ApiRequestActions

class ApiRequest(ApiRequestBase, ApiRequestActions):
    '''
    classdocs
    '''
    def __init__(self, currentrequestindex=None, maxrequests=None, param=[], cloudid=None):
        '''
        Constructor
        @param currentrequestindex: currentrequestindex
        @type currentrequestindex: int
        @param maxrequests: maxrequests
        @type maxrequests: int
        @param param: param minOccurs=0 maxOccurs=unbounded
        @type param: Property
        @param cloudid: cloudid
        @type cloudid: int
        '''
        ApiRequestBase.__init__(self, currentrequestindex=currentrequestindex, maxrequests=maxrequests, param=param, cloudid=cloudid)
