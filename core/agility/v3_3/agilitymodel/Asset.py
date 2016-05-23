from core.agility.v3_3.agilitymodel.base.Asset import AssetBase
from core.agility.v3_3.agilitymodel.actions.Asset import AssetActions

class Asset(AssetBase, AssetActions):
    '''
    classdocs
    '''
    def __init__(self, importmode=None, lifecyclelastcomment=None, asset=[], assetpath=None, foreignassetproperties=[], top=False, detailedassetpath=None, lifecycleversion=None, description=None, assettype=None, importdirectives=None, usedbyassets=[], removable=None, id=None, assetlist=[], tags=None, assetproperties=[], uuid=None, applicationtype=None, lifecyclestate=None):
        '''
        Constructor
        @param importmode: importmode minOccurs=0
        @type importmode: ImportMode
        @param lifecyclelastcomment: lifecyclelastcomment minOccurs=0
        @type lifecyclelastcomment: string
        @param asset: asset minOccurs=0 maxOccurs=unbounded
        @type asset: Asset
        @param assetpath: assetpath minOccurs=0
        @type assetpath: string
        @param foreignassetproperties: foreignassetproperties minOccurs=0 maxOccurs=unbounded
        @type foreignassetproperties: ForeignAssetProperty
        @param top: top
        @type top: boolean
        @param detailedassetpath: detailedassetpath minOccurs=0
        @type detailedassetpath: string
        @param lifecycleversion: lifecycleversion minOccurs=0
        @type lifecycleversion: int
        @param description: description minOccurs=0
        @type description: string
        @param assettype: assettype minOccurs=0
        @type assettype: Link
        @param importdirectives: importdirectives minOccurs=0
        @type importdirectives: ImportDirectives
        @param usedbyassets: usedbyassets minOccurs=0 maxOccurs=unbounded
        @type usedbyassets: Link
        @param removable: removable minOccurs=0
        @type removable: boolean
        @param id: id minOccurs=0
        @type id: int
        @param assetlist: assetlist minOccurs=0 maxOccurs=unbounded
        @type assetlist: Assetlist
        @param tags: tags minOccurs=0
        @type tags: string
        @param assetproperties: assetproperties minOccurs=0 maxOccurs=unbounded
        @type assetproperties: AssetProperty
        @param uuid: uuid minOccurs=0
        @type uuid: string
        @param applicationtype: applicationtype minOccurs=0
        @type applicationtype: string
        @param lifecyclestate: lifecyclestate minOccurs=0
        @type lifecyclestate: string
        '''
        AssetBase.__init__(self, importmode=importmode, lifecyclelastcomment=lifecyclelastcomment, asset=asset, assetpath=assetpath, foreignassetproperties=foreignassetproperties, top=top, detailedassetpath=detailedassetpath, lifecycleversion=lifecycleversion, description=description, assettype=assettype, importdirectives=importdirectives, usedbyassets=usedbyassets, removable=removable, id=id, assetlist=assetlist, tags=tags, assetproperties=assetproperties, uuid=uuid, applicationtype=applicationtype, lifecyclestate=lifecyclestate)
