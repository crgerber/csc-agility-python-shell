from core.agility.v2_0.agilitymodel.base.AssetFilter import AssetFilterBase
from core.agility.v2_0.agilitymodel.actions.AssetFilter import AssetFilterActions

class AssetFilter(AssetFilterBase, AssetFilterActions):
    '''
    classdocs
    '''
    def __init__(self, item=list(), eval=list(), match=list()):
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
