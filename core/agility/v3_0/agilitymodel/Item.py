from core.agility.v3_0.agilitymodel.base.Item import ItemBase
from core.agility.v3_0.agilitymodel.actions.Item import ItemActions

class Item(ItemBase, ItemActions):
    '''
    classdocs
    '''
    def __init__(self, domain=None, parent=None, created=None, lastmodified=None, creator=None, policyassignment=[], locktype=None):
        '''
        Constructor
        @param domain: domain minOccurs=0
        @type domain: Link
        @param parent: parent minOccurs=0
        @type parent: Link
        @param created: created minOccurs=0
        @type created: date
        @param lastmodified: lastmodified minOccurs=0
        @type lastmodified: date
        @param creator: creator minOccurs=0
        @type creator: Link
        @param policyassignment: policyassignment minOccurs=0 maxOccurs=unbounded
        @type policyassignment: PolicyAssignment
        @param locktype: locktype minOccurs=0
        @type locktype: int
        '''
        ItemBase.__init__(self, domain=domain, parent=parent, created=created, lastmodified=lastmodified, creator=creator, policyassignment=policyassignment, locktype=locktype)
