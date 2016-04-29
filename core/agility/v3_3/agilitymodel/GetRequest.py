from core.agility.v3_3.agilitymodel.base.GetRequest import GetRequestBase
from core.agility.v3_3.agilitymodel.actions.GetRequest import GetRequestActions

class GetRequest(GetRequestBase, GetRequestActions):
    '''
    classdocs
    '''
    def __init__(self, id=None, type=''):
        '''
        Constructor
        @param id: id
        @type id: int
        @param type: type
        @type type: string
        '''
        GetRequestBase.__init__(self, id=id, type=type)
