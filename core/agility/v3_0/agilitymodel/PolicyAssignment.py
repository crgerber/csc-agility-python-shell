from core.agility.v3_0.agilitymodel.base.PolicyAssignment import PolicyAssignmentBase
from core.agility.v3_0.agilitymodel.actions.PolicyAssignment import PolicyAssignmentActions

class PolicyAssignment(PolicyAssignmentBase, PolicyAssignmentActions):
    '''
    classdocs
    '''
    def __init__(self, itemid=None, itemclass=None, policytypename=None, inherited=None, permissioned=None, applychildrendepth=None, allowchildrenoverride=False, policy=None, filtermatch=None, itemname=None, applytoself=False):
        '''
        Constructor
        @param itemid: itemid minOccurs=0
        @type itemid: int
        @param itemclass: itemclass minOccurs=0
        @type itemclass: string
        @param policytypename: policytypename minOccurs=0
        @type policytypename: string
        @param inherited: inherited minOccurs=0
        @type inherited: boolean
        @param permissioned: permissioned minOccurs=0
        @type permissioned: boolean
        @param applychildrendepth: applychildrendepth minOccurs=0
        @type applychildrendepth: int
        @param allowchildrenoverride: allowchildrenoverride
        @type allowchildrenoverride: boolean
        @param policy: policy minOccurs=0
        @type policy: Link
        @param filtermatch: filtermatch minOccurs=0
        @type filtermatch: boolean
        @param itemname: itemname minOccurs=0
        @type itemname: string
        @param applytoself: applytoself
        @type applytoself: boolean
        '''
        PolicyAssignmentBase.__init__(self, itemid=itemid, itemclass=itemclass, policytypename=policytypename, inherited=inherited, permissioned=permissioned, applychildrendepth=applychildrendepth, allowchildrenoverride=allowchildrenoverride, policy=policy, filtermatch=filtermatch, itemname=itemname, applytoself=applytoself)
