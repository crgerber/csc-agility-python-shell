from core.agility.v3_3.agilitymodel.base.Proxy import ProxyBase
from core.agility.v3_3.agilitymodel.actions.Proxy import ProxyActions

class Proxy(ProxyBase, ProxyActions):
    '''
    classdocs
    '''
    def __init__(self, credentials=None, proxyusage=None, authtype=None, proxytype=None, hostname=None, port=None):
        '''
        Constructor
        @param credentials: credentials minOccurs=0
        @type credentials: Credential
        @param proxyusage: proxyusage minOccurs=0
        @type proxyusage: ProxyUsage
        @param authtype: authtype minOccurs=0
        @type authtype: AuthType
        @param proxytype: proxytype minOccurs=0
        @type proxytype: ProxyType
        @param hostname: hostname minOccurs=0
        @type hostname: string
        @param port: port minOccurs=0
        @type port: int
        '''
        ProxyBase.__init__(self, credentials=credentials, proxyusage=proxyusage, authtype=authtype, proxytype=proxytype, hostname=hostname, port=port)
