from core.agility.v3_3.agilitymodel.base.AccessRightSet import AccessRightSetBase
from core.agility.v3_3.agilitymodel.actions.AccessRightSet import AccessRightSetActions

class AccessRightSet(AccessRightSetBase, AccessRightSetActions):
    '''
    classdocs
    '''
    def __init__(self, accessright=[], name=None, description=None, id=None, filter=None):
        '''
        Constructor
        @param accessright: accessright minOccurs=0 maxOccurs=unbounded
        @type accessright: AccessRight
        @param name: name minOccurs=0
        @type name: string
        @param description: description minOccurs=0
        @type description: string
        @param id: id minOccurs=0
        @type id: int
        @param filter: filter minOccurs=0
        @type filter: string
        '''
        AccessRightSetBase.__init__(self, accessright=accessright, name=name, description=description, id=id, filter=filter)
