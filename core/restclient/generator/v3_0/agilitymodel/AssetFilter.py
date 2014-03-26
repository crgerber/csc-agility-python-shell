from base.AssetFilter import AssetFilterBase
from actions.AssetFilter import AssetFilterActions

class AssetFilter(AssetFilterBase, AssetFilterActions):
    '''
    classdocs
    '''
    def __init__(self, item=[], eval=[], match=[]):
        '''
        Constructor
        @param item: item minOccurs=0 maxOccurs=unbounded
        @type item: Link
        @param eval: eval minOccurs=0 maxOccurs=unbounded
        @type eval: Script
        @param match: match minOccurs=0 maxOccurs=unbounded
        @type match: AssetMatch
        '''
        AssetFilterBase.__init__(self, item=item, eval=eval, match=match)
