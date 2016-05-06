from core.agility.v3_3.agilitymodel.base.ApiResponse import ApiResponseBase
from core.agility.v3_3.agilitymodel.actions.ApiResponse import ApiResponseActions

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
