from core.restclient.v2_0.agilitymodel.base.Asset import AssetBase
from core.restclient.v2_0.agilitymodel.actions.Asset import AssetActions

class Asset(AssetBase, AssetActions):
    '''
    classdocs
    '''
    def __init__(self, assetType=None, usedByAssets=list(), importMode=None, uuid=None, detailedAssetPath=None, tags=None, assetProperties=list(), top=False, importDirectives=None, name=None, lifecycleVersion=None, Assetlist=list(), Asset=list(), removable=None, lifecycleLastComment=None, assetPath=None, lifecycleState=None, id=None, applicationType=None, description=None):
        '''
        Constructor
        @param assetType: assetType minOccurs=0
        @type assetType: Link
        @param usedByAssets: usedByAssets minOccurs=0 maxOccurs=unbounded
        @type usedByAssets: Link
        @param importMode: importMode minOccurs=0
        @type importMode: ImportMode
        @param uuid: uuid minOccurs=0
        @type uuid: string
        @param detailedAssetPath: detailedAssetPath minOccurs=0
        @type detailedAssetPath: string
        @param tags: tags minOccurs=0
        @type tags: string
        @param assetProperties: assetProperties minOccurs=0 maxOccurs=unbounded
        @type assetProperties: AssetProperty
        @param top: top
        @type top: boolean
        @param importDirectives: importDirectives minOccurs=0
        @type importDirectives: ImportDirectives
        @param name: name minOccurs=0
        @type name: string
        @param lifecycleVersion: lifecycleVersion minOccurs=0
        @type lifecycleVersion: int
        @param Assetlist: Assetlist minOccurs=0 maxOccurs=unbounded
        @type Assetlist: Assetlist
        @param Asset: Asset minOccurs=0 maxOccurs=unbounded
        @type Asset: Asset
        @param removable: removable minOccurs=0
        @type removable: boolean
        @param lifecycleLastComment: lifecycleLastComment minOccurs=0
        @type lifecycleLastComment: string
        @param assetPath: assetPath minOccurs=0
        @type assetPath: string
        @param lifecycleState: lifecycleState minOccurs=0
        @type lifecycleState: string
        @param id: id minOccurs=0
        @type id: int
        @param applicationType: applicationType minOccurs=0
        @type applicationType: string
        @param description: description minOccurs=0
        @type description: string
        '''
        AssetBase.__init__(self, assetType=assetType, usedByAssets=usedByAssets, importMode=importMode, uuid=uuid, detailedAssetPath=detailedAssetPath, tags=tags, assetProperties=assetProperties, top=top, importDirectives=importDirectives, name=name, lifecycleVersion=lifecycleVersion, Assetlist=Assetlist, Asset=Asset, removable=removable, lifecycleLastComment=lifecycleLastComment, assetPath=assetPath, lifecycleState=lifecycleState, id=id, applicationType=applicationType, description=description)
