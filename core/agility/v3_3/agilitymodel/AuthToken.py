from core.agility.v3_3.agilitymodel.base.AuthToken import AuthTokenBase
from core.agility.v3_3.agilitymodel.actions.AuthToken import AuthTokenActions

class AuthToken(AuthTokenBase, AuthTokenActions):
    '''
    classdocs
    '''
    def __init__(self, id=None, token=None, created=None):
        '''
        Constructor
        @param id: id minOccurs=0
        @type id: int
        @param token: token minOccurs=0
        @type token: string
        @param created: created minOccurs=0
        @type created: dateTime
        '''
        AuthTokenBase.__init__(self, id=id, token=token, created=created)
