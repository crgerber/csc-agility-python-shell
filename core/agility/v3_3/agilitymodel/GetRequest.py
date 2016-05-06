from core.agility.v3_3.agilitymodel.base.GetRequest import GetRequestBase
from core.agility.v3_3.agilitymodel.actions.GetRequest import GetRequestActions

class GetRequest(GetRequestBase, GetRequestActions):
    '''
    classdocs
    '''
    def __init__(self, type='', id=None):
        '''
        Constructor
        @param type: type
        @type type: string
        @param id: id
        @type id: int
        '''
        GetRequestBase.__init__(self, type=type, id=id)
