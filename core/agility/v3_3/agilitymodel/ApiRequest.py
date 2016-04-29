from core.agility.v3_3.agilitymodel.base.ApiRequest import ApiRequestBase
from core.agility.v3_3.agilitymodel.actions.ApiRequest import ApiRequestActions

class ApiRequest(ApiRequestBase, ApiRequestActions):
    '''
    classdocs
    '''
    def __init__(self, maxrequests=None, cloudid=None, currentrequestindex=None, param=[]):
        '''
        Constructor
        @param maxrequests: maxrequests
        @type maxrequests: int
        @param cloudid: cloudid
        @type cloudid: int
        @param currentrequestindex: currentrequestindex
        @type currentrequestindex: int
        @param param: param minOccurs=0 maxOccurs=unbounded
        @type param: Property
        '''
        ApiRequestBase.__init__(self, maxrequests=maxrequests, cloudid=cloudid, currentrequestindex=currentrequestindex, param=param)
