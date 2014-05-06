from base.AccessRight import AccessRightBase
from actions.AccessRight import AccessRightActions

class AccessRight(AccessRightBase, AccessRightActions):
    '''
    classdocs
    '''
    def __init__(self, source=None, defaultgranted=None, granted=None, id=None, name=None):
        '''
        Constructor
        @param source: source minOccurs=0
        @type source: string
        @param defaultgranted: defaultgranted minOccurs=0
        @type defaultgranted: boolean
        @param granted: granted minOccurs=0
        @type granted: boolean
        @param id: id minOccurs=0
        @type id: int
        @param name: name minOccurs=0
        @type name: string
        '''
        AccessRightBase.__init__(self, source=source, defaultgranted=defaultgranted, granted=granted, id=id, name=name)
