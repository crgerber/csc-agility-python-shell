from base.AssetMatch import AssetMatchBase
from actions.AssetMatch import AssetMatchActions

class AssetMatch(AssetMatchBase, AssetMatchActions):
    '''
    classdocs
    '''
    def __init__(self, property=list(), type='', name=None):
        '''
        Constructor
        @param property: property minOccurs=0 maxOccurs=unbounded
        @type property: PropertyMatch
        @param type: type
        @type type: string
        @param name: name minOccurs=0
        @type name: string
        '''
        AssetMatchBase.__init__(self, property=property, type=type, name=name)
