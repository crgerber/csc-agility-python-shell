from base.AccessRightSet import AccessRightSetBase
from actions.AccessRightSet import AccessRightSetActions

class AccessRightSet(AccessRightSetBase, AccessRightSetActions):
    '''
    classdocs
    '''
    def __init__(self, filter=None, description=None, accessright=[], id=None, name=None):
        '''
        Constructor
        @param filter: filter minOccurs=0
        @type filter: string
        @param description: description minOccurs=0
        @type description: string
        @param accessright: accessright minOccurs=0 maxOccurs=unbounded
        @type accessright: AccessRight
        @param id: id minOccurs=0
        @type id: int
        @param name: name minOccurs=0
        @type name: string
        '''
        AccessRightSetBase.__init__(self, filter=filter, description=description, accessright=accessright, id=id, name=name)
