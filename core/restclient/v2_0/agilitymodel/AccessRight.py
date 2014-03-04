from core.restclient.v2_0.agilitymodel.base.AccessRight import AccessRightBase
from core.restclient.v2_0.agilitymodel.actions.AccessRight import AccessRightActions

class AccessRight(AccessRightBase, AccessRightActions):
    '''
    classdocs
    '''
    def __init__(self, source=None, defaultGranted=None, granted=None, id=None, name=None):
        '''
        Constructor
        @param source: source minOccurs=0
        @type source: string
        @param defaultGranted: defaultGranted minOccurs=0
        @type defaultGranted: boolean
        @param granted: granted minOccurs=0
        @type granted: boolean
        @param id: id minOccurs=0
        @type id: int
        @param name: name minOccurs=0
        @type name: string
        '''
        AccessRightBase.__init__(self, source=source, defaultGranted=defaultGranted, granted=granted, id=id, name=name)
