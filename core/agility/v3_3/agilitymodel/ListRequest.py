from base.ListRequest import ListRequestBase
from actions.ListRequest import ListRequestActions

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
