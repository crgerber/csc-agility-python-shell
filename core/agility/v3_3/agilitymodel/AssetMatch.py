from core.agility.v3_3.agilitymodel.base.AssetMatch import AssetMatchBase
from core.agility.v3_3.agilitymodel.actions.AssetMatch import AssetMatchActions

class AssetMatch(AssetMatchBase, AssetMatchActions):
    '''
    classdocs
    '''
    def __init__(self, name=None, type='', property=[]):
        '''
        Constructor
        @param name: name minOccurs=0
        @type name: string
        @param type: type
        @type type: string
        @param property: property minOccurs=0 maxOccurs=unbounded
        @type property: PropertyMatch
        '''
        AssetMatchBase.__init__(self, name=name, type=type, property=property)
