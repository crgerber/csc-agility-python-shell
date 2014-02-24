from base.User import UserBase
from actions.User import UserActions

class User(UserBase, UserActions):
    '''
    classdocs
    '''
    def __init__(self, sshKey=None, enabled=None, accessRights=list(), groups=list(), password=None, email=None, digest=None):
        '''
        Constructor
        @param sshKey: sshKey minOccurs=0
        @type sshKey: Credential
        @param enabled: enabled minOccurs=0
        @type enabled: boolean
        @param accessRights: accessRights minOccurs=0 maxOccurs=unbounded
        @type accessRights: AccessRight
        @param groups: groups minOccurs=0 maxOccurs=unbounded
        @type groups: Link
        @param password: password minOccurs=0
        @type password: string
        @param email: email minOccurs=0
        @type email: string
        @param digest: digest minOccurs=0
        @type digest: string
        '''
        UserBase.__init__(self, sshKey=sshKey, enabled=enabled, accessRights=accessRights, groups=groups, password=password, email=email, digest=digest)
