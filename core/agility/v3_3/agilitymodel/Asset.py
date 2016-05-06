from core.agility.v3_3.agilitymodel.base.Asset import AssetBase
from core.agility.v3_3.agilitymodel.actions.Asset import AssetActions

class Asset(AssetBase, AssetActions):
    '''
    classdocs
    '''
    def __init__(self, assettype=None, usedbyassets=[], importmode=None, uuid=None, detailedassetpath=None, tags=None, assetproperties=[], foreignassetproperties=[], top=False, importdirectives=None, lifecycleversion=None, assetlist=[], asset=[], removable=None, lifecyclelastcomment=None, assetpath=None, lifecyclestate=None, id=None, applicationtype=None, description=None):
        '''
        Constructor
        @param assettype: assettype minOccurs=0
        @type assettype: Link
        @param usedbyassets: usedbyassets minOccurs=0 maxOccurs=unbounded
        @type usedbyassets: Link
        @param importmode: importmode minOccurs=0
        @type importmode: ImportMode
        @param uuid: uuid minOccurs=0
        @type uuid: string
        @param detailedassetpath: detailedassetpath minOccurs=0
        @type detailedassetpath: string
        @param tags: tags minOccurs=0
        @type tags: string
        @param assetproperties: assetproperties minOccurs=0 maxOccurs=unbounded
        @type assetproperties: AssetProperty
        @param foreignassetproperties: foreignassetproperties minOccurs=0 maxOccurs=unbounded
        @type foreignassetproperties: ForeignAssetProperty
        @param top: top
        @type top: boolean
        @param importdirectives: importdirectives minOccurs=0
        @type importdirectives: ImportDirectives
        @param lifecycleversion: lifecycleversion minOccurs=0
        @type lifecycleversion: int
        @param assetlist: assetlist minOccurs=0 maxOccurs=unbounded
        @type assetlist: Assetlist
        @param asset: asset minOccurs=0 maxOccurs=unbounded
        @type asset: Asset
        @param removable: removable minOccurs=0
        @type removable: boolean
        @param lifecyclelastcomment: lifecyclelastcomment minOccurs=0
        @type lifecyclelastcomment: string
        @param assetpath: assetpath minOccurs=0
        @type assetpath: string
        @param lifecyclestate: lifecyclestate minOccurs=0
        @type lifecyclestate: string
        @param id: id minOccurs=0
        @type id: int
        @param applicationtype: applicationtype minOccurs=0
        @type applicationtype: string
        @param description: description minOccurs=0
        @type description: string
        '''
        AssetBase.__init__(self, assettype=assettype, usedbyassets=usedbyassets, importmode=importmode, uuid=uuid, detailedassetpath=detailedassetpath, tags=tags, assetproperties=assetproperties, foreignassetproperties=foreignassetproperties, top=top, importdirectives=importdirectives, lifecycleversion=lifecycleversion, assetlist=assetlist, asset=asset, removable=removable, lifecyclelastcomment=lifecyclelastcomment, assetpath=assetpath, lifecyclestate=lifecyclestate, id=id, applicationtype=applicationtype, description=description)
