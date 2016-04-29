from core.agility.v3_3.agilitymodel.base.DistNode import DistNodeBase
from core.agility.v3_3.agilitymodel.actions.DistNode import DistNodeActions

class DistNode(DistNodeBase, DistNodeActions):
    '''
    classdocs
    '''
    def __init__(self, ipaddress=None, version=None, nodestatus=None, packages=[], nodetype=None, state=None, hostname=None):
        '''
        Constructor
        @param ipaddress: ipaddress minOccurs=0
        @type ipaddress: string
        @param version: version minOccurs=0
        @type version: string
        @param nodestatus: nodestatus minOccurs=0
        @type nodestatus: string
        @param packages: packages minOccurs=0 maxOccurs=unbounded
        @type packages: DistNodePackage
        @param nodetype: nodetype minOccurs=0
        @type nodetype: string
        @param state: state minOccurs=0
        @type state: State
        @param hostname: hostname minOccurs=0
        @type hostname: string
        '''
        DistNodeBase.__init__(self, ipaddress=ipaddress, version=version, nodestatus=nodestatus, packages=packages, nodetype=nodetype, state=state, hostname=hostname)
