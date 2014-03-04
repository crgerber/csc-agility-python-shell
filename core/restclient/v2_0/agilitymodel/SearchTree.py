from core.restclient.v2_0.agilitymodel.base.SearchTree import SearchTreeBase
from core.restclient.v2_0.agilitymodel.actions.SearchTree import SearchTreeActions

class SearchTree(SearchTreeBase, SearchTreeActions):
    '''
    classdocs
    '''
    def __init__(self, Assetlist=list()):
        '''
        Constructor
        @param Assetlist: Assetlist minOccurs=0 maxOccurs=unbounded
        @type Assetlist: Assetlist
        '''
        SearchTreeBase.__init__(self, Assetlist=Assetlist)
