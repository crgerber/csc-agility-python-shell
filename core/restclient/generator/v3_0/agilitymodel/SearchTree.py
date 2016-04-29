from .base.SearchTree import SearchTreeBase
from .actions.SearchTree import SearchTreeActions

class SearchTree(SearchTreeBase, SearchTreeActions):
    '''
    classdocs
    '''
    def __init__(self, assetlist=[]):
        '''
        Constructor
        @param assetlist: assetlist minOccurs=0 maxOccurs=unbounded
        @type assetlist: Assetlist
        '''
        SearchTreeBase.__init__(self, assetlist=assetlist)
