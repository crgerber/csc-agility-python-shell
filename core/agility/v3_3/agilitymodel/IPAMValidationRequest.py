from core.agility.v3_3.agilitymodel.base.IPAMValidationRequest import IPAMValidationRequestBase
from core.agility.v3_3.agilitymodel.actions.IPAMValidationRequest import IPAMValidationRequestActions

class IPAMValidationRequest(IPAMValidationRequestBase, IPAMValidationRequestActions):
    '''
    classdocs
    '''
    def __init__(self, crudoperation=None, serviceprovider=None):
        '''
        Constructor
        @param crudoperation: crudoperation
        @type crudoperation: IPAMValidationCRUDType
        @param serviceprovider: serviceprovider minOccurs=0
        @type serviceprovider: ServiceProvider
        '''
        IPAMValidationRequestBase.__init__(self, crudoperation=crudoperation, serviceprovider=serviceprovider)
