from core.agility.v3_3.agilitymodel.base.AccessRight import AccessRightBase
from core.agility.v3_3.agilitymodel.actions.AccessRight import AccessRightActions

class AccessRight(AccessRightBase, AccessRightActions):
    '''
    classdocs
    '''
    def __init__(self, id=None, name=None, granted=None, defaultgranted=None, source=None):
        '''
        Constructor
        @param id: id minOccurs=0
        @type id: int
        @param name: name minOccurs=0
        @type name: string
        @param granted: granted minOccurs=0
        @type granted: boolean
        @param defaultgranted: defaultgranted minOccurs=0
        @type defaultgranted: boolean
        @param source: source minOccurs=0
        @type source: string
        '''
        AccessRightBase.__init__(self, id=id, name=name, granted=granted, defaultgranted=defaultgranted, source=source)
