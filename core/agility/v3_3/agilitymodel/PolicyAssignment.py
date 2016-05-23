from core.agility.v3_3.agilitymodel.base.PolicyAssignment import PolicyAssignmentBase
from core.agility.v3_3.agilitymodel.actions.PolicyAssignment import PolicyAssignmentActions

class PolicyAssignment(PolicyAssignmentBase, PolicyAssignmentActions):
    '''
    classdocs
    '''
    def __init__(self, permissioned=None, allowchildrenoverride=False, inherited=None, itemname=None, itemclass=None, applychildrendepth=None, policy=None, itemid=None, applytoself=False, policytypename=None, filtermatch=None):
        '''
        Constructor
        @param permissioned: permissioned minOccurs=0
        @type permissioned: boolean
        @param allowchildrenoverride: allowchildrenoverride
        @type allowchildrenoverride: boolean
        @param inherited: inherited minOccurs=0
        @type inherited: boolean
        @param itemname: itemname minOccurs=0
        @type itemname: string
        @param itemclass: itemclass minOccurs=0
        @type itemclass: string
        @param applychildrendepth: applychildrendepth minOccurs=0
        @type applychildrendepth: int
        @param policy: policy minOccurs=0
        @type policy: Link
        @param itemid: itemid minOccurs=0
        @type itemid: int
        @param applytoself: applytoself
        @type applytoself: boolean
        @param policytypename: policytypename minOccurs=0
        @type policytypename: string
        @param filtermatch: filtermatch minOccurs=0
        @type filtermatch: boolean
        '''
        PolicyAssignmentBase.__init__(self, permissioned=permissioned, allowchildrenoverride=allowchildrenoverride, inherited=inherited, itemname=itemname, itemclass=itemclass, applychildrendepth=applychildrendepth, policy=policy, itemid=itemid, applytoself=applytoself, policytypename=policytypename, filtermatch=filtermatch)
