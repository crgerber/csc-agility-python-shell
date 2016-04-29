from core.agility.v3_3.agilitymodel.base.AccessRight import AccessRightBase
from core.agility.v3_3.agilitymodel.actions.AccessRight import AccessRightActions

class AccessRight(AccessRightBase, AccessRightActions):
    '''
    classdocs
    '''
    def __init__(self, granted=None, name=None, defaultgranted=None, source=None, id=None):
        '''
        Constructor
        @param granted: granted minOccurs=0
        @type granted: boolean
        @param name: name minOccurs=0
        @type name: string
        @param defaultgranted: defaultgranted minOccurs=0
        @type defaultgranted: boolean
        @param source: source minOccurs=0
        @type source: string
        @param id: id minOccurs=0
        @type id: int
        '''
        AccessRightBase.__init__(self, granted=granted, name=name, defaultgranted=defaultgranted, source=source, id=id)
