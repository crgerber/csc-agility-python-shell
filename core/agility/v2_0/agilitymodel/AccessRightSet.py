from core.agility.v2_0.agilitymodel.base.AccessRightSet import AccessRightSetBase
from core.agility.v2_0.agilitymodel.actions.AccessRightSet import AccessRightSetActions

class AccessRightSet(AccessRightSetBase, AccessRightSetActions):
    '''
    classdocs
    '''
    def __init__(self, filter=None, description=None, accessRight=list(), id=None, name=None):
        '''
        Constructor
        @param filter: filter minOccurs=0
        @type filter: string
        @param description: description minOccurs=0
        @type description: string
        @param accessRight: accessRight minOccurs=0 maxOccurs=unbounded
        @type accessRight: AccessRight
        @param id: id minOccurs=0
        @type id: int
        @param name: name minOccurs=0
        @type name: string
        '''
        AccessRightSetBase.__init__(self, filter=filter, description=description, accessRight=accessRight, id=id, name=name)
