from core.agility.v3_3.agilitymodel.base.User import UserBase
from core.agility.v3_3.agilitymodel.actions.User import UserActions

class User(UserBase, UserActions):
    '''
    classdocs
    '''
    def __init__(self, password=None, digestiterations=None, accessrights=[], sshkey=None, digestsalt=None, enabled=None, externaluser=None, digestalgorithm=None, email=None, digest=None, digestexpiration=None, groups=[]):
        '''
        Constructor
        @param password: password minOccurs=0
        @type password: string
        @param digestiterations: digestiterations minOccurs=0
        @type digestiterations: int
        @param accessrights: accessrights minOccurs=0 maxOccurs=unbounded
        @type accessrights: AccessRight
        @param sshkey: sshkey minOccurs=0
        @type sshkey: Credential
        @param digestsalt: digestsalt minOccurs=0
        @type digestsalt: string
        @param enabled: enabled minOccurs=0
        @type enabled: boolean
        @param externaluser: externaluser minOccurs=0
        @type externaluser: boolean
        @param digestalgorithm: digestalgorithm minOccurs=0
        @type digestalgorithm: string
        @param email: email minOccurs=0
        @type email: string
        @param digest: digest minOccurs=0
        @type digest: string
        @param digestexpiration: digestexpiration minOccurs=0
        @type digestexpiration: date
        @param groups: groups minOccurs=0 maxOccurs=unbounded
        @type groups: Link
        '''
        UserBase.__init__(self, password=password, digestiterations=digestiterations, accessrights=accessrights, sshkey=sshkey, digestsalt=digestsalt, enabled=enabled, externaluser=externaluser, digestalgorithm=digestalgorithm, email=email, digest=digest, digestexpiration=digestexpiration, groups=groups)
