from core.agility.v3_3.agilitymodel.base.Asset import AssetBase
from core.agility.v3_3.agilitymodel.actions.Asset import AssetActions

class Asset(AssetBase, AssetActions):
    '''
    classdocs
    '''
    def __init__(self, lifecycleversion=None, uuid=None, asset=[], tags=None, assetlist=[], assetproperties=[], lifecyclestate=None, assetpath=None, id=None, detailedassetpath=None, top=False, removable=None, assettype=None, description=None, usedbyassets=[], importmode=None, foreignassetproperties=[], lifecyclelastcomment=None, applicationtype=None, importdirectives=None):
        '''
        Constructor
        @param lifecycleversion: lifecycleversion minOccurs=0
        @type lifecycleversion: int
        @param uuid: uuid minOccurs=0
        @type uuid: string
        @param asset: asset minOccurs=0 maxOccurs=unbounded
        @type asset: Asset
        @param tags: tags minOccurs=0
        @type tags: string
        @param assetlist: assetlist minOccurs=0 maxOccurs=unbounded
        @type assetlist: Assetlist
        @param assetproperties: assetproperties minOccurs=0 maxOccurs=unbounded
        @type assetproperties: AssetProperty
        @param lifecyclestate: lifecyclestate minOccurs=0
        @type lifecyclestate: string
        @param assetpath: assetpath minOccurs=0
        @type assetpath: string
        @param id: id minOccurs=0
        @type id: int
        @param detailedassetpath: detailedassetpath minOccurs=0
        @type detailedassetpath: string
        @param top: top
        @type top: boolean
        @param removable: removable minOccurs=0
        @type removable: boolean
        @param assettype: assettype minOccurs=0
        @type assettype: Link
        @param description: description minOccurs=0
        @type description: string
        @param usedbyassets: usedbyassets minOccurs=0 maxOccurs=unbounded
        @type usedbyassets: Link
        @param importmode: importmode minOccurs=0
        @type importmode: ImportMode
        @param foreignassetproperties: foreignassetproperties minOccurs=0 maxOccurs=unbounded
        @type foreignassetproperties: ForeignAssetProperty
        @param lifecyclelastcomment: lifecyclelastcomment minOccurs=0
        @type lifecyclelastcomment: string
        @param applicationtype: applicationtype minOccurs=0
        @type applicationtype: string
        @param importdirectives: importdirectives minOccurs=0
        @type importdirectives: ImportDirectives
        '''
        AssetBase.__init__(self, lifecycleversion=lifecycleversion, uuid=uuid, asset=asset, tags=tags, assetlist=assetlist, assetproperties=assetproperties, lifecyclestate=lifecyclestate, assetpath=assetpath, id=id, detailedassetpath=detailedassetpath, top=top, removable=removable, assettype=assettype, description=description, usedbyassets=usedbyassets, importmode=importmode, foreignassetproperties=foreignassetproperties, lifecyclelastcomment=lifecyclelastcomment, applicationtype=applicationtype, importdirectives=importdirectives)
