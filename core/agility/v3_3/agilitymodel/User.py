from core.agility.v3_3.agilitymodel.base.User import UserBase
from core.agility.v3_3.agilitymodel.actions.User import UserActions

class User(UserBase, UserActions):
    '''
    classdocs
    '''
    def __init__(self, groups=[], digestexpiration=None, digest=None, accessrights=[], sshkey=None, email=None, digestiterations=None, password=None, externaluser=None, enabled=None, digestsalt=None, digestalgorithm=None):
        '''
        Constructor
        @param groups: groups minOccurs=0 maxOccurs=unbounded
        @type groups: Link
        @param digestexpiration: digestexpiration minOccurs=0
        @type digestexpiration: date
        @param digest: digest minOccurs=0
        @type digest: string
        @param accessrights: accessrights minOccurs=0 maxOccurs=unbounded
        @type accessrights: AccessRight
        @param sshkey: sshkey minOccurs=0
        @type sshkey: Credential
        @param email: email minOccurs=0
        @type email: string
        @param digestiterations: digestiterations minOccurs=0
        @type digestiterations: int
        @param password: password minOccurs=0
        @type password: string
        @param externaluser: externaluser minOccurs=0
        @type externaluser: boolean
        @param enabled: enabled minOccurs=0
        @type enabled: boolean
        @param digestsalt: digestsalt minOccurs=0
        @type digestsalt: string
        @param digestalgorithm: digestalgorithm minOccurs=0
        @type digestalgorithm: string
        '''
        UserBase.__init__(self, groups=groups, digestexpiration=digestexpiration, digest=digest, accessrights=accessrights, sshkey=sshkey, email=email, digestiterations=digestiterations, password=password, externaluser=externaluser, enabled=enabled, digestsalt=digestsalt, digestalgorithm=digestalgorithm)
