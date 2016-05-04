from core.agility.v3_3.agilitymodel.base.VolumeResponse import VolumeResponseBase
from core.agility.v3_3.agilitymodel.actions.VolumeResponse import VolumeResponseActions

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
