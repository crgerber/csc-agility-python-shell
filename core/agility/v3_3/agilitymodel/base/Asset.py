from core.agility.v3_3.agilitymodel.base.Baselink import BaselinkBase

class AssetBase(BaselinkBase):
    '''
    classdocs
    '''
    def __init__(self, importmode=None, lifecyclelastcomment=None, asset=[], assetpath=None, foreignassetproperties=[], top=False, detailedassetpath=None, lifecycleversion=None, description=None, assettype=None, importdirectives=None, usedbyassets=[], removable=None, id=None, assetlist=[], tags=None, assetproperties=[], uuid=None, applicationtype=None, lifecyclestate=None):
        BaselinkBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'importMode': {'name': 'importmode', 'minOccurs': '0', 'native': False, 'type': 'ImportMode'}, 'lifecycleState': {'name': 'lifecyclestate', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'Asset': {'name': 'asset', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Asset'}, 'uuid': {'name': 'uuid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'top': {'name': 'top', 'native': True, 'type': 'boolean'}, 'detailedAssetPath': {'name': 'detailedassetpath', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'lifecycleVersion': {'name': 'lifecycleversion', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'foreignAssetProperties': {'name': 'foreignassetproperties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'ForeignAssetProperty'}, 'assetType': {'name': 'assettype', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'usedByAssets': {'name': 'usedbyassets', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'importDirectives': {'name': 'importdirectives', 'minOccurs': '0', 'native': False, 'type': 'ImportDirectives'}, 'description': {'name': 'description', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'removable': {'name': 'removable', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'id': {'name': 'id', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'Assetlist': {'name': 'assetlist', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Assetlist'}, 'tags': {'name': 'tags', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'assetProperties': {'name': 'assetproperties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetProperty'}, 'assetPath': {'name': 'assetpath', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'applicationType': {'name': 'applicationtype', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'lifecycleLastComment': {'name': 'lifecyclelastcomment', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.importmode = importmode
        self.lifecyclelastcomment = lifecyclelastcomment
        self.asset = asset
        self.assetpath = assetpath
        self.foreignassetproperties = foreignassetproperties
        self.top = top
        self.detailedassetpath = detailedassetpath
        self.lifecycleversion = lifecycleversion
        self.description = description
        self.assettype = assettype
        self.importdirectives = importdirectives
        self.usedbyassets = usedbyassets
        self.removable = removable
        self.id = id
        self.assetlist = assetlist
        self.tags = tags
        self.assetproperties = assetproperties
        self.uuid = uuid
        self.applicationtype = applicationtype
        self.lifecyclestate = lifecyclestate 
