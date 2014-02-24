from base.Proxy import ProxyBase
from actions.Proxy import ProxyActions

class Proxy(ProxyBase, ProxyActions):
    '''
    classdocs
    '''
    def __init__(self, proxyType=None, authType=None, proxyUsage=None, hostname=None, credentials=None, port=None):
        '''
        Constructor
        @param proxyType: proxyType minOccurs=0
        @type proxyType: ProxyType
        @param authType: authType minOccurs=0
        @type authType: AuthType
        @param proxyUsage: proxyUsage minOccurs=0
        @type proxyUsage: ProxyUsage
        @param hostname: hostname minOccurs=0
        @type hostname: string
        @param credentials: credentials minOccurs=0
        @type credentials: Credential
        @param port: port minOccurs=0
        @type port: int
        '''
        ProxyBase.__init__(self, proxyType=proxyType, authType=authType, proxyUsage=proxyUsage, hostname=hostname, credentials=credentials, port=port)
