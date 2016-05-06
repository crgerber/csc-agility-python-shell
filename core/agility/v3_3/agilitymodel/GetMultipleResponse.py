from core.agility.v3_3.agilitymodel.base.GetMultipleResponse import GetMultipleResponseBase
from core.agility.v3_3.agilitymodel.actions.GetMultipleResponse import GetMultipleResponseActions

class GetMultipleResponse(GetMultipleResponseBase, GetMultipleResponseActions):
    '''
    classdocs
    '''
    def __init__(self, asset=[]):
        '''
        Constructor
        @param asset: asset minOccurs=0 maxOccurs=unbounded
        @type asset: Asset
        '''
        GetMultipleResponseBase.__init__(self, asset=asset)
