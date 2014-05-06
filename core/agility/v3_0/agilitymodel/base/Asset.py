from core.agility.common.AgilityModelBase import AgilityModelBase


class AssetBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, assettype=None, usedbyassets=[], importmode=None, uuid=None, detailedassetpath=None, tags=None, assetproperties=[], foreignassetproperties=[], top=False, importdirectives=None, name=None, lifecycleversion=None, assetlist=[], asset=[], removable=None, lifecyclelastcomment=None, assetpath=None, lifecyclestate=None, id=None, applicationtype=None, description=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'assetType': {'type': 'Link', 'name': 'assettype', 'minOccurs': '0', 'native': False}, 'usedByAssets': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'usedbyassets', 'minOccurs': '0', 'native': False}, 'importMode': {'type': 'ImportMode', 'name': 'importmode', 'minOccurs': '0', 'native': False}, 'uuid': {'type': 'string', 'name': 'uuid', 'minOccurs': '0', 'native': True}, 'tags': {'type': 'string', 'name': 'tags', 'minOccurs': '0', 'native': True}, 'assetProperties': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'assetproperties', 'minOccurs': '0', 'native': False}, 'foreignAssetProperties': {'maxOccurs': 'unbounded', 'type': 'ForeignAssetProperty', 'name': 'foreignassetproperties', 'minOccurs': '0', 'native': False}, 'top': {'type': 'boolean', 'name': 'top', 'native': True}, 'description': {'type': 'string', 'name': 'description', 'minOccurs': '0', 'native': True}, 'importDirectives': {'type': 'ImportDirectives', 'name': 'importdirectives', 'minOccurs': '0', 'native': False}, 'lifecycleVersion': {'type': 'int', 'name': 'lifecycleversion', 'minOccurs': '0', 'native': True}, 'Assetlist': {'maxOccurs': 'unbounded', 'type': 'Assetlist', 'name': 'assetlist', 'minOccurs': '0', 'native': False}, 'lifecycleState': {'type': 'string', 'name': 'lifecyclestate', 'minOccurs': '0', 'native': True}, 'Asset': {'maxOccurs': 'unbounded', 'type': 'Asset', 'name': 'asset', 'minOccurs': '0', 'native': False}, 'removable': {'type': 'boolean', 'name': 'removable', 'minOccurs': '0', 'native': True}, 'lifecycleLastComment': {'type': 'string', 'name': 'lifecyclelastcomment', 'minOccurs': '0', 'native': True}, 'detailedAssetPath': {'type': 'string', 'name': 'detailedassetpath', 'minOccurs': '0', 'native': True}, 'assetPath': {'type': 'string', 'name': 'assetpath', 'minOccurs': '0', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'minOccurs': '0', 'native': True}, 'applicationType': {'type': 'string', 'name': 'applicationtype', 'minOccurs': '0', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'minOccurs': '0', 'native': True}})
        self.assettype = assettype
        self.usedbyassets = usedbyassets
        self.importmode = importmode
        self.uuid = uuid
        self.detailedassetpath = detailedassetpath
        self.tags = tags
        self.assetproperties = assetproperties
        self.foreignassetproperties = foreignassetproperties
        self.top = top
        self.importdirectives = importdirectives
        self.name = name
        self.lifecycleversion = lifecycleversion
        self.assetlist = assetlist
        self.asset = asset
        self.removable = removable
        self.lifecyclelastcomment = lifecyclelastcomment
        self.assetpath = assetpath
        self.lifecyclestate = lifecyclestate
        self.id = id
        self.applicationtype = applicationtype
        self.description = description 
