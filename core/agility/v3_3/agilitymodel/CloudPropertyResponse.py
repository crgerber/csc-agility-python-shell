from core.agility.v3_3.agilitymodel.base.CloudPropertyResponse import CloudPropertyResponseBase
from core.agility.v3_3.agilitymodel.actions.CloudPropertyResponse import CloudPropertyResponseActions

class CloudPropertyResponse(CloudPropertyResponseBase, CloudPropertyResponseActions):
    '''
    classdocs
    '''
    def __init__(self, value=False):
        '''
        Constructor
        @param value: value
        @type value: boolean
        '''
        CloudPropertyResponseBase.__init__(self, value=value)
