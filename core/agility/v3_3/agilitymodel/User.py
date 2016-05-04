from base.User import UserBase
from actions.User import UserActions

class User(UserBase, UserActions):
    '''
    classdocs
    '''
    def __init__(self, digestiterations=None, sshkey=None, digestalgorithm=None, digestsalt=None, enabled=None, accessrights=[], externaluser=None, groups=[], digestexpiration=None, password=None, email=None, digest=None):
        '''
        Constructor
        @param digestiterations: digestiterations minOccurs=0
        @type digestiterations: int
        @param sshkey: sshkey minOccurs=0
        @type sshkey: Credential
        @param digestalgorithm: digestalgorithm minOccurs=0
        @type digestalgorithm: string
        @param digestsalt: digestsalt minOccurs=0
        @type digestsalt: string
        @param enabled: enabled minOccurs=0
        @type enabled: boolean
        @param accessrights: accessrights minOccurs=0 maxOccurs=unbounded
        @type accessrights: AccessRight
        @param externaluser: externaluser minOccurs=0
        @type externaluser: boolean
        @param groups: groups minOccurs=0 maxOccurs=unbounded
        @type groups: Link
        @param digestexpiration: digestexpiration minOccurs=0
        @type digestexpiration: date
        @param password: password minOccurs=0
        @type password: string
        @param email: email minOccurs=0
        @type email: string
        @param digest: digest minOccurs=0
        @type digest: string
        '''
        UserBase.__init__(self, digestiterations=digestiterations, sshkey=sshkey, digestalgorithm=digestalgorithm, digestsalt=digestsalt, enabled=enabled, accessrights=accessrights, externaluser=externaluser, groups=groups, digestexpiration=digestexpiration, password=password, email=email, digest=digest)
