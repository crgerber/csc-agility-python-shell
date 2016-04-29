from .base.PermissionType import PermissionTypeBase
from .actions.PermissionType import PermissionTypeActions

class PermissionType(PermissionTypeBase, PermissionTypeActions):
    '''
    classdocs
    '''
    def __init__(self, global_=None, displayname=None):
        '''
        Constructor
        @param global_: global_ minOccurs=0
        @type global_: boolean
        @param displayname: displayname minOccurs=0
        @type displayname: string
        '''
        PermissionTypeBase.__init__(self, global_=global_, displayname=displayname)
