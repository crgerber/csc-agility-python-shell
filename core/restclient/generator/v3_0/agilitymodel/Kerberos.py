from .base.Kerberos import KerberosBase
from .actions.Kerberos import KerberosActions

class Kerberos(KerberosBase, KerberosActions):
    '''
    classdocs
    '''
    def __init__(self, hostname='', enabled=None, domainrealm=''):
        '''
        Constructor
        @param hostname: hostname
        @type hostname: string
        @param enabled: enabled minOccurs=0
        @type enabled: boolean
        @param domainrealm: domainrealm
        @type domainrealm: string
        '''
        KerberosBase.__init__(self, hostname=hostname, enabled=enabled, domainrealm=domainrealm)
