from core.agility.v3_0.agilitymodel.base.Account import AccountBase
from core.agility.v3_0.agilitymodel.actions.Account import AccountActions

class Account(AccountBase, AccountActions):
    '''
    classdocs
    '''
    def __init__(self, credentials=None, enabled=None, domainname=''):
        '''
        Constructor
        @param credentials: credentials minOccurs=0
        @type credentials: Credential
        @param enabled: enabled minOccurs=0
        @type enabled: boolean
        @param domainname: domainname
        @type domainname: string
        '''
        AccountBase.__init__(self, credentials=credentials, enabled=enabled, domainname=domainname)
