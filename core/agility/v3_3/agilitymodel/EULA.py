from core.agility.v3_3.agilitymodel.base.EULA import EULABase
from core.agility.v3_3.agilitymodel.actions.EULA import EULAActions

class EULA(EULABase, EULAActions):
    '''
    classdocs
    '''
    def __init__(self, timestamp=None, title='', valid=False, readonly=False, signature='', agreedto=False, eula='', adminuser=False, company=''):
        '''
        Constructor
        @param timestamp: timestamp minOccurs=0
        @type timestamp: date
        @param title: title
        @type title: string
        @param valid: valid
        @type valid: boolean
        @param readonly: readonly
        @type readonly: boolean
        @param signature: signature
        @type signature: string
        @param agreedto: agreedto
        @type agreedto: boolean
        @param eula: eula
        @type eula: string
        @param adminuser: adminuser
        @type adminuser: boolean
        @param company: company
        @type company: string
        '''
        EULABase.__init__(self, timestamp=timestamp, title=title, valid=valid, readonly=readonly, signature=signature, agreedto=agreedto, eula=eula, adminuser=adminuser, company=company)
