from core.agility.v3_3.agilitymodel.base.AssetTypeBrief import AssetTypeBriefBase
from core.agility.v3_3.agilitymodel.actions.AssetTypeBrief import AssetTypeBriefActions

class AssetTypeBrief(AssetTypeBriefBase, AssetTypeBriefActions):
    '''
    classdocs
    '''
    def __init__(self, entitytype='', path='', name='', displayname='', jaxbtype='', id=None):
        '''
        Constructor
        @param entitytype: entitytype
        @type entitytype: string
        @param path: path
        @type path: string
        @param name: name
        @type name: string
        @param displayname: displayname
        @type displayname: string
        @param jaxbtype: jaxbtype
        @type jaxbtype: string
        @param id: id
        @type id: int
        '''
        AssetTypeBriefBase.__init__(self, entitytype=entitytype, path=path, name=name, displayname=displayname, jaxbtype=jaxbtype, id=id)
