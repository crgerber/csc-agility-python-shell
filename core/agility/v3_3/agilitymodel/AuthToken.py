from core.agility.v3_3.agilitymodel.base.AuthToken import AuthTokenBase
from core.agility.v3_3.agilitymodel.actions.AuthToken import AuthTokenActions

class AuthToken(AuthTokenBase, AuthTokenActions):
    '''
    classdocs
    '''
    def __init__(self, token=None, id=None, created=None):
        '''
        Constructor
        @param token: token minOccurs=0
        @type token: string
        @param id: id minOccurs=0
        @type id: int
        @param created: created minOccurs=0
        @type created: dateTime
        '''
        AuthTokenBase.__init__(self, token=token, id=id, created=created)
