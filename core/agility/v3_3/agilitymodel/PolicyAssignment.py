from core.agility.v3_3.agilitymodel.base.PolicyAssignment import PolicyAssignmentBase
from core.agility.v3_3.agilitymodel.actions.PolicyAssignment import PolicyAssignmentActions

class PolicyAssignment(PolicyAssignmentBase, PolicyAssignmentActions):
    '''
    classdocs
    '''
    def __init__(self, inherited=None, itemname=None, applytoself=False, filtermatch=None, allowchildrenoverride=False, applychildrendepth=None, policytypename=None, itemid=None, itemclass=None, permissioned=None, policy=None):
        '''
        Constructor
        @param inherited: inherited minOccurs=0
        @type inherited: boolean
        @param itemname: itemname minOccurs=0
        @type itemname: string
        @param applytoself: applytoself
        @type applytoself: boolean
        @param filtermatch: filtermatch minOccurs=0
        @type filtermatch: boolean
        @param allowchildrenoverride: allowchildrenoverride
        @type allowchildrenoverride: boolean
        @param applychildrendepth: applychildrendepth minOccurs=0
        @type applychildrendepth: int
        @param policytypename: policytypename minOccurs=0
        @type policytypename: string
        @param itemid: itemid minOccurs=0
        @type itemid: int
        @param itemclass: itemclass minOccurs=0
        @type itemclass: string
        @param permissioned: permissioned minOccurs=0
        @type permissioned: boolean
        @param policy: policy minOccurs=0
        @type policy: Link
        '''
        PolicyAssignmentBase.__init__(self, inherited=inherited, itemname=itemname, applytoself=applytoself, filtermatch=filtermatch, allowchildrenoverride=allowchildrenoverride, applychildrendepth=applychildrendepth, policytypename=policytypename, itemid=itemid, itemclass=itemclass, permissioned=permissioned, policy=policy)
