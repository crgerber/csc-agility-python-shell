from .base.User import UserBase
from .actions.User import UserActions

class User(UserBase, UserActions):
    '''
    classdocs
    '''
    def __init__(self, sshkey=None, enabled=None, accessrights=[], uselocalauth=None, groups=[], password=None, email=None, digest=None):
        '''
        Constructor
        @param sshkey: sshkey minOccurs=0
        @type sshkey: Credential
        @param enabled: enabled minOccurs=0
        @type enabled: boolean
        @param accessrights: accessrights minOccurs=0 maxOccurs=unbounded
        @type accessrights: AccessRight
        @param uselocalauth: uselocalauth minOccurs=0
        @type uselocalauth: boolean
        @param groups: groups minOccurs=0 maxOccurs=unbounded
        @type groups: Link
        @param password: password minOccurs=0
        @type password: string
        @param email: email minOccurs=0
        @type email: string
        @param digest: digest minOccurs=0
        @type digest: string
        '''
        UserBase.__init__(self, sshkey=sshkey, enabled=enabled, accessrights=accessrights, uselocalauth=uselocalauth, groups=groups, password=password, email=email, digest=digest)
