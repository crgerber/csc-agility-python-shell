from core.agility.v3_3.agilitymodel.base.EULA import EULABase
from core.agility.v3_3.agilitymodel.actions.EULA import EULAActions

class EULA(EULABase, EULAActions):
    '''
    classdocs
    '''
    def __init__(self, eula='', signature='', agreedto=False, adminuser=False, readonly=False, timestamp=None, valid=False, title='', company=''):
        '''
        Constructor
        @param eula: eula
        @type eula: string
        @param signature: signature
        @type signature: string
        @param agreedto: agreedto
        @type agreedto: boolean
        @param adminuser: adminuser
        @type adminuser: boolean
        @param readonly: readonly
        @type readonly: boolean
        @param timestamp: timestamp minOccurs=0
        @type timestamp: date
        @param valid: valid
        @type valid: boolean
        @param title: title
        @type title: string
        @param company: company
        @type company: string
        '''
        EULABase.__init__(self, eula=eula, signature=signature, agreedto=agreedto, adminuser=adminuser, readonly=readonly, timestamp=timestamp, valid=valid, title=title, company=company)
