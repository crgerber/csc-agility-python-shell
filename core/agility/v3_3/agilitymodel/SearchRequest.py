from base.SearchRequest import SearchRequestBase
from actions.SearchRequest import SearchRequestActions

class SearchRequest(SearchRequestBase, SearchRequestActions):
    '''
    classdocs
    '''
    def __init__(self, type=''):
        '''
        Constructor
        @param type: type
        @type type: string
        '''
        SearchRequestBase.__init__(self, type=type)
