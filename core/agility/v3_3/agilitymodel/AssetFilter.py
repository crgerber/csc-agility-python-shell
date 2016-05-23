from core.agility.v3_3.agilitymodel.base.AssetFilter import AssetFilterBase
from core.agility.v3_3.agilitymodel.actions.AssetFilter import AssetFilterActions

class AssetFilter(AssetFilterBase, AssetFilterActions):
    '''
    classdocs
    '''
    def __init__(self, eval=[], match=[], item=[]):
        '''
        Constructor
        @param eval: eval minOccurs=0 maxOccurs=unbounded
        @type eval: Script
        @param match: match minOccurs=0 maxOccurs=unbounded
        @type match: AssetMatch
        @param item: item minOccurs=0 maxOccurs=unbounded
        @type item: Link
        '''
        AssetFilterBase.__init__(self, eval=eval, match=match, item=item)
