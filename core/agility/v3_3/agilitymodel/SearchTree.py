from core.agility.v3_3.agilitymodel.base.SearchTree import SearchTreeBase
from core.agility.v3_3.agilitymodel.actions.SearchTree import SearchTreeActions

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
