from core.agility.v3_3.agilitymodel.base.ListRequest import ListRequestBase
from core.agility.v3_3.agilitymodel.actions.ListRequest import ListRequestActions

class ListRequest(ListRequestBase, ListRequestActions):
    '''
    classdocs
    '''
    def __init__(self, type=''):
        '''
        Constructor
        @param type: type
        @type type: string
        '''
        ListRequestBase.__init__(self, type=type)
