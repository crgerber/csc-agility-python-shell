from .base.AssetTypeBrief import AssetTypeBriefBase
from .actions.AssetTypeBrief import AssetTypeBriefActions

class AssetTypeBrief(AssetTypeBriefBase, AssetTypeBriefActions):
    '''
    classdocs
    '''
    def __init__(self, entitytype='', displayname='', id=None, jaxbtype='', name=''):
        '''
        Constructor
        @param entitytype: entitytype
        @type entitytype: string
        @param displayname: displayname
        @type displayname: string
        @param id: id
        @type id: int
        @param jaxbtype: jaxbtype
        @type jaxbtype: string
        @param name: name
        @type name: string
        '''
        AssetTypeBriefBase.__init__(self, entitytype=entitytype, displayname=displayname, id=id, jaxbtype=jaxbtype, name=name)
