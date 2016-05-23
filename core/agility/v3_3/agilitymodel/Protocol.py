from core.agility.v3_3.agilitymodel.base.Protocol import ProtocolBase
from core.agility.v3_3.agilitymodel.actions.Protocol import ProtocolActions

class Protocol(ProtocolBase, ProtocolActions):
    '''
    classdocs
    '''
    def __init__(self, maxport=None, allowed=None, minport=None, prefixes=[], protocol=None):
        '''
        Constructor
        @param maxport: maxport minOccurs=0
        @type maxport: int
        @param allowed: allowed minOccurs=0
        @type allowed: boolean
        @param minport: minport minOccurs=0
        @type minport: int
        @param prefixes: prefixes minOccurs=0 maxOccurs=unbounded
        @type prefixes: string
        @param protocol: protocol minOccurs=0
        @type protocol: string
        '''
        ProtocolBase.__init__(self, maxport=maxport, allowed=allowed, minport=minport, prefixes=prefixes, protocol=protocol)
