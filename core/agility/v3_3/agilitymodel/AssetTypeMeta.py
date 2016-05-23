from core.agility.v3_3.agilitymodel.base.AssetTypeMeta import AssetTypeMetaBase
from core.agility.v3_3.agilitymodel.actions.AssetTypeMeta import AssetTypeMetaActions

class AssetTypeMeta(AssetTypeMetaBase, AssetTypeMetaActions):
    '''
    classdocs
    '''
    def __init__(self, name='', applicableassignmenttype=[], displayname='', supportedeventtype=[]):
        '''
        Constructor
        @param name: name
        @type name: string
        @param applicableassignmenttype: applicableassignmenttype minOccurs=0 maxOccurs=unbounded
        @type applicableassignmenttype: string
        @param displayname: displayname
        @type displayname: string
        @param supportedeventtype: supportedeventtype minOccurs=0 maxOccurs=unbounded
        @type supportedeventtype: string
        '''
        AssetTypeMetaBase.__init__(self, name=name, applicableassignmenttype=applicableassignmenttype, displayname=displayname, supportedeventtype=supportedeventtype)
