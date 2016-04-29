from core.agility.v3_3.agilitymodel.base.AssetTypeMeta import AssetTypeMetaBase
from core.agility.v3_3.agilitymodel.actions.AssetTypeMeta import AssetTypeMetaActions

class AssetTypeMeta(AssetTypeMetaBase, AssetTypeMetaActions):
    '''
    classdocs
    '''
    def __init__(self, supportedeventtype=[], name='', displayname='', applicableassignmenttype=[]):
        '''
        Constructor
        @param supportedeventtype: supportedeventtype minOccurs=0 maxOccurs=unbounded
        @type supportedeventtype: string
        @param name: name
        @type name: string
        @param displayname: displayname
        @type displayname: string
        @param applicableassignmenttype: applicableassignmenttype minOccurs=0 maxOccurs=unbounded
        @type applicableassignmenttype: string
        '''
        AssetTypeMetaBase.__init__(self, supportedeventtype=supportedeventtype, name=name, displayname=displayname, applicableassignmenttype=applicableassignmenttype)
