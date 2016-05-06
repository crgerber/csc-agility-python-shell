from core.agility.v3_3.agilitymodel.base.DistNode import DistNodeBase
from core.agility.v3_3.agilitymodel.actions.DistNode import DistNodeActions

class DistNode(DistNodeBase, DistNodeActions):
    '''
    classdocs
    '''
    def __init__(self, nodetype=None, nodestatus=None, hostname=None, state=None, version=None, packages=[], ipaddress=None):
        '''
        Constructor
        @param nodetype: nodetype minOccurs=0
        @type nodetype: string
        @param nodestatus: nodestatus minOccurs=0
        @type nodestatus: string
        @param hostname: hostname minOccurs=0
        @type hostname: string
        @param state: state minOccurs=0
        @type state: State
        @param version: version minOccurs=0
        @type version: string
        @param packages: packages minOccurs=0 maxOccurs=unbounded
        @type packages: DistNodePackage
        @param ipaddress: ipaddress minOccurs=0
        @type ipaddress: string
        '''
        DistNodeBase.__init__(self, nodetype=nodetype, nodestatus=nodestatus, hostname=hostname, state=state, version=version, packages=packages, ipaddress=ipaddress)
