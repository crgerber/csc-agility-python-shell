from base.Protocol import ProtocolBase
from actions.Protocol import ProtocolActions

class Protocol(ProtocolBase, ProtocolActions):
    '''
    classdocs
    '''
    def __init__(self, prefixes=[], protocol=None, minport=None, maxport=None, allowed=None):
        '''
        Constructor
        @param prefixes: prefixes minOccurs=0 maxOccurs=unbounded
        @type prefixes: string
        @param protocol: protocol minOccurs=0
        @type protocol: string
        @param minport: minport minOccurs=0
        @type minport: int
        @param maxport: maxport minOccurs=0
        @type maxport: int
        @param allowed: allowed minOccurs=0
        @type allowed: boolean
        '''
        ProtocolBase.__init__(self, prefixes=prefixes, protocol=protocol, minport=minport, maxport=maxport, allowed=allowed)
