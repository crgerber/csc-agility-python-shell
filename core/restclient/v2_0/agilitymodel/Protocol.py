from core.restclient.v2_0.agilitymodel.base.Protocol import ProtocolBase
from core.restclient.v2_0.agilitymodel.actions.Protocol import ProtocolActions

class Protocol(ProtocolBase, ProtocolActions):
    '''
    classdocs
    '''
    def __init__(self, prefixes=list(), protocol=None, minPort=None, maxPort=None, allowed=None):
        '''
        Constructor
        @param prefixes: prefixes minOccurs=0 maxOccurs=unbounded
        @type prefixes: string
        @param protocol: protocol minOccurs=0
        @type protocol: string
        @param minPort: minPort minOccurs=0
        @type minPort: int
        @param maxPort: maxPort minOccurs=0
        @type maxPort: int
        @param allowed: allowed minOccurs=0
        @type allowed: boolean
        '''
        ProtocolBase.__init__(self, prefixes=prefixes, protocol=protocol, minPort=minPort, maxPort=maxPort, allowed=allowed)
