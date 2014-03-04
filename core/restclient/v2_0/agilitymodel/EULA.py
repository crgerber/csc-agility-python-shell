from core.restclient.v2_0.agilitymodel.base.EULA import EULABase
from core.restclient.v2_0.agilitymodel.actions.EULA import EULAActions

class EULA(EULABase, EULAActions):
    '''
    classdocs
    '''
    def __init__(self, eula='', adminUser=False, title='', timestamp=None, company='', signature='', readOnly=False, valid=False, agreedTo=False):
        '''
        Constructor
        @param eula: eula
        @type eula: string
        @param adminUser: adminUser
        @type adminUser: boolean
        @param title: title
        @type title: string
        @param timestamp: timestamp minOccurs=0
        @type timestamp: date
        @param company: company
        @type company: string
        @param signature: signature
        @type signature: string
        @param readOnly: readOnly
        @type readOnly: boolean
        @param valid: valid
        @type valid: boolean
        @param agreedTo: agreedTo
        @type agreedTo: boolean
        '''
        EULABase.__init__(self, eula=eula, adminUser=adminUser, title=title, timestamp=timestamp, company=company, signature=signature, readOnly=readOnly, valid=valid, agreedTo=agreedTo)
