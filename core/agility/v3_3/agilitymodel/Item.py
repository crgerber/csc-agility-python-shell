from core.agility.v3_3.agilitymodel.base.Item import ItemBase
from core.agility.v3_3.agilitymodel.actions.Item import ItemActions

class Item(ItemBase, ItemActions):
    '''
    classdocs
    '''
    def __init__(self, created=None, creator=None, lastmodified=None, locktype=None, domain=None, parent=None, policyassignment=[]):
        '''
        Constructor
        @param created: created minOccurs=0
        @type created: date
        @param creator: creator minOccurs=0
        @type creator: Link
        @param lastmodified: lastmodified minOccurs=0
        @type lastmodified: date
        @param locktype: locktype minOccurs=0
        @type locktype: int
        @param domain: domain minOccurs=0
        @type domain: Link
        @param parent: parent minOccurs=0
        @type parent: Link
        @param policyassignment: policyassignment minOccurs=0 maxOccurs=unbounded
        @type policyassignment: PolicyAssignment
        '''
        ItemBase.__init__(self, created=created, creator=creator, lastmodified=lastmodified, locktype=locktype, domain=domain, parent=parent, policyassignment=policyassignment)
