from core.agility.v3_3.agilitymodel.base.IPAMValidationResponse import IPAMValidationResponseBase
from core.agility.v3_3.agilitymodel.actions.IPAMValidationResponse import IPAMValidationResponseActions

class IPAMValidationResponse(IPAMValidationResponseBase, IPAMValidationResponseActions):
    '''
    classdocs
    '''
    def __init__(self, errormessage=None):
        '''
        Constructor
        @param errormessage: errormessage minOccurs=0
        @type errormessage: string
        '''
        IPAMValidationResponseBase.__init__(self, errormessage=errormessage)
