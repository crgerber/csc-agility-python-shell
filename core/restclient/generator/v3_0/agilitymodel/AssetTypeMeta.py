from base.AssetTypeMeta import AssetTypeMetaBase
from actions.AssetTypeMeta import AssetTypeMetaActions

class AssetTypeMeta(AssetTypeMetaBase, AssetTypeMetaActions):
    '''
    classdocs
    '''
    def __init__(self, applicableassignmenttype=[], supportedeventtype=[], displayname='', name=''):
        '''
        Constructor
        @param applicableassignmenttype: applicableassignmenttype minOccurs=0 maxOccurs=unbounded
        @type applicableassignmenttype: string
        @param supportedeventtype: supportedeventtype minOccurs=0 maxOccurs=unbounded
        @type supportedeventtype: string
        @param displayname: displayname
        @type displayname: string
        @param name: name
        @type name: string
        '''
        AssetTypeMetaBase.__init__(self, applicableassignmenttype=applicableassignmenttype, supportedeventtype=supportedeventtype, displayname=displayname, name=name)
