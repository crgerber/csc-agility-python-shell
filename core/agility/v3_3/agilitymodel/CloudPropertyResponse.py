from base.CloudPropertyResponse import CloudPropertyResponseBase
from actions.CloudPropertyResponse import CloudPropertyResponseActions

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
