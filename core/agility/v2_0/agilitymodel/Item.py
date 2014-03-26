from core.agility.v2_0.agilitymodel.base.Item import ItemBase
from core.agility.v2_0.agilitymodel.actions.Item import ItemActions

class Item(ItemBase, ItemActions):
    '''
    classdocs
    '''
    def __init__(self, domain=None, parent=None, created=None, lastModified=None, creator=None, policyAssignment=list(), lockType=None):
        '''
        Constructor
        @param domain: domain minOccurs=0
        @type domain: Link
        @param parent: parent minOccurs=0
        @type parent: Link
        @param created: created minOccurs=0
        @type created: date
        @param lastModified: lastModified minOccurs=0
        @type lastModified: date
        @param creator: creator minOccurs=0
        @type creator: Link
        @param policyAssignment: policyAssignment minOccurs=0 maxOccurs=unbounded
        @type policyAssignment: PolicyAssignment
        @param lockType: lockType minOccurs=0
        @type lockType: int
        '''
        ItemBase.__init__(self, domain=domain, parent=parent, created=created, lastModified=lastModified, creator=creator, policyAssignment=policyAssignment, lockType=lockType)
