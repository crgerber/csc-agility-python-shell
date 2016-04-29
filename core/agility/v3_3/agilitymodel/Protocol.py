from core.agility.v3_3.agilitymodel.base.Protocol import ProtocolBase
from core.agility.v3_3.agilitymodel.actions.Protocol import ProtocolActions

class Protocol(ProtocolBase, ProtocolActions):
    '''
    classdocs
    '''
    def __init__(self, prefixes=[], maxport=None, protocol=None, minport=None, allowed=None):
        '''
        Constructor
        @param prefixes: prefixes minOccurs=0 maxOccurs=unbounded
        @type prefixes: string
        @param maxport: maxport minOccurs=0
        @type maxport: int
        @param protocol: protocol minOccurs=0
        @type protocol: string
        @param minport: minport minOccurs=0
        @type minport: int
        @param allowed: allowed minOccurs=0
        @type allowed: boolean
        '''
        ProtocolBase.__init__(self, prefixes=prefixes, maxport=maxport, protocol=protocol, minport=minport, allowed=allowed)
