from core.agility.v3_3.agilitymodel.base.EULA import EULABase
from core.agility.v3_3.agilitymodel.actions.EULA import EULAActions

class EULA(EULABase, EULAActions):
    '''
    classdocs
    '''
    def __init__(self, eula='', adminuser=False, title='', timestamp=None, company='', signature='', readonly=False, valid=False, agreedto=False):
        '''
        Constructor
        @param eula: eula
        @type eula: string
        @param adminuser: adminuser
        @type adminuser: boolean
        @param title: title
        @type title: string
        @param timestamp: timestamp minOccurs=0
        @type timestamp: date
        @param company: company
        @type company: string
        @param signature: signature
        @type signature: string
        @param readonly: readonly
        @type readonly: boolean
        @param valid: valid
        @type valid: boolean
        @param agreedto: agreedto
        @type agreedto: boolean
        '''
        EULABase.__init__(self, eula=eula, adminuser=adminuser, title=title, timestamp=timestamp, company=company, signature=signature, readonly=readonly, valid=valid, agreedto=agreedto)
