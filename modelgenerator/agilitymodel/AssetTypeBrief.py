from base.AssetTypeBrief import AssetTypeBriefBase
from actions.AssetTypeBrief import AssetTypeBriefActions

class AssetTypeBrief(AssetTypeBriefBase, AssetTypeBriefActions):
    '''
    classdocs
    '''
    def __init__(self, entityType='', displayName='', id=None, jaxbType='', name=''):
        '''
        Constructor
        @param entityType: entityType
        @type entityType: string
        @param displayName: displayName
        @type displayName: string
        @param id: id
        @type id: int
        @param jaxbType: jaxbType
        @type jaxbType: string
        @param name: name
        @type name: string
        '''
        AssetTypeBriefBase.__init__(self, entityType=entityType, displayName=displayName, id=id, jaxbType=jaxbType, name=name)
