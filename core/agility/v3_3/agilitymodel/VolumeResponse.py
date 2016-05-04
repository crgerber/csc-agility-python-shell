from base.VolumeResponse import VolumeResponseBase
from actions.VolumeResponse import VolumeResponseActions

class VolumeResponse(VolumeResponseBase, VolumeResponseActions):
    '''
    classdocs
    '''
    def __init__(self, errormessage=None):
        '''
        Constructor
        @param errormessage: errormessage minOccurs=0
        @type errormessage: string
        '''
        VolumeResponseBase.__init__(self, errormessage=errormessage)
