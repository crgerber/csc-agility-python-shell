from base.ApiResponse import ApiResponseBase
from actions.ApiResponse import ApiResponseActions

class ApiResponse(ApiResponseBase, ApiResponseActions):
    '''
    classdocs
    '''
    def __init__(self, currentrequestindex=None, maxrequests=None, asset=None):
        '''
        Constructor
        @param currentrequestindex: currentrequestindex
        @type currentrequestindex: int
        @param maxrequests: maxrequests
        @type maxrequests: int
        @param asset: asset minOccurs=0
        @type asset: Asset
        '''
        ApiResponseBase.__init__(self, currentrequestindex=currentrequestindex, maxrequests=maxrequests, asset=asset)
