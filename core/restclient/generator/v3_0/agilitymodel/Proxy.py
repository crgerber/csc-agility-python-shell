from base.Proxy import ProxyBase
from actions.Proxy import ProxyActions

class Proxy(ProxyBase, ProxyActions):
    '''
    classdocs
    '''
    def __init__(self, proxytype=None, authtype=None, proxyusage=None, hostname=None, credentials=None, port=None):
        '''
        Constructor
        @param proxytype: proxytype minOccurs=0
        @type proxytype: ProxyType
        @param authtype: authtype minOccurs=0
        @type authtype: AuthType
        @param proxyusage: proxyusage minOccurs=0
        @type proxyusage: ProxyUsage
        @param hostname: hostname minOccurs=0
        @type hostname: string
        @param credentials: credentials minOccurs=0
        @type credentials: Credential
        @param port: port minOccurs=0
        @type port: int
        '''
        ProxyBase.__init__(self, proxytype=proxytype, authtype=authtype, proxyusage=proxyusage, hostname=hostname, credentials=credentials, port=port)
