from core.agility.v3_3.agilitymodel.base.AccessRightSet import AccessRightSetBase
from core.agility.v3_3.agilitymodel.actions.AccessRightSet import AccessRightSetActions

class AccessRightSet(AccessRightSetBase, AccessRightSetActions):
    '''
    classdocs
    '''
    def __init__(self, id=None, name=None, accessright=[], filter=None, description=None):
        '''
        Constructor
        @param id: id minOccurs=0
        @type id: int
        @param name: name minOccurs=0
        @type name: string
        @param accessright: accessright minOccurs=0 maxOccurs=unbounded
        @type accessright: AccessRight
        @param filter: filter minOccurs=0
        @type filter: string
        @param description: description minOccurs=0
        @type description: string
        '''
        AccessRightSetBase.__init__(self, id=id, name=name, accessright=accessright, filter=filter, description=description)
