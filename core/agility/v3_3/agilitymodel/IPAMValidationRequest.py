from core.agility.v3_3.agilitymodel.base.IPAMValidationRequest import IPAMValidationRequestBase
from core.agility.v3_3.agilitymodel.actions.IPAMValidationRequest import IPAMValidationRequestActions

class IPAMValidationRequest(IPAMValidationRequestBase, IPAMValidationRequestActions):
    '''
    classdocs
    '''
    def __init__(self, serviceprovider=None, crudoperation=None):
        '''
        Constructor
        @param serviceprovider: serviceprovider minOccurs=0
        @type serviceprovider: ServiceProvider
        @param crudoperation: crudoperation
        @type crudoperation: IPAMValidationCRUDType
        '''
        IPAMValidationRequestBase.__init__(self, serviceprovider=serviceprovider, crudoperation=crudoperation)
