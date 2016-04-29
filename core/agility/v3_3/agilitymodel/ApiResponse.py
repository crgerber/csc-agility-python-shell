from core.agility.v3_3.agilitymodel.base.ApiResponse import ApiResponseBase
from core.agility.v3_3.agilitymodel.actions.ApiResponse import ApiResponseActions

class ApiResponse(ApiResponseBase, ApiResponseActions):
    '''
    classdocs
    '''
    def __init__(self, asset=None, currentrequestindex=None, maxrequests=None):
        '''
        Constructor
        @param asset: asset minOccurs=0
        @type asset: Asset
        @param currentrequestindex: currentrequestindex
        @type currentrequestindex: int
        @param maxrequests: maxrequests
        @type maxrequests: int
        '''
        ApiResponseBase.__init__(self, asset=asset, currentrequestindex=currentrequestindex, maxrequests=maxrequests)
