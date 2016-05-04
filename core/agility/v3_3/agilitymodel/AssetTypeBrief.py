from core.agility.v3_3.agilitymodel.base.AssetTypeBrief import AssetTypeBriefBase
from core.agility.v3_3.agilitymodel.actions.AssetTypeBrief import AssetTypeBriefActions

class AssetTypeBrief(AssetTypeBriefBase, AssetTypeBriefActions):
    '''
    classdocs
    '''
    def __init__(self, displayname='', name='', entitytype='', jaxbtype='', path='', id=None):
        '''
        Constructor
        @param displayname: displayname
        @type displayname: string
        @param name: name
        @type name: string
        @param entitytype: entitytype
        @type entitytype: string
        @param jaxbtype: jaxbtype
        @type jaxbtype: string
        @param path: path
        @type path: string
        @param id: id
        @type id: int
        '''
        AssetTypeBriefBase.__init__(self, displayname=displayname, name=name, entitytype=entitytype, jaxbtype=jaxbtype, path=path, id=id)
