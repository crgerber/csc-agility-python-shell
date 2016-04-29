from core.agility.v3_3.agilitymodel.base.Baselink import BaselinkBase

class AssetBase(BaselinkBase):
    '''
    classdocs
    '''
    def __init__(self, lifecycleversion=None, uuid=None, asset=[], tags=None, assetlist=[], assetproperties=[], lifecyclestate=None, assetpath=None, id=None, detailedassetpath=None, top=False, removable=None, assettype=None, description=None, usedbyassets=[], importmode=None, foreignassetproperties=[], lifecyclelastcomment=None, applicationtype=None, importdirectives=None):
        BaselinkBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'lifecycleVersion': {'native': True, 'name': 'lifecycleversion', 'minOccurs': '0', 'type': 'int'}, 'uuid': {'native': True, 'name': 'uuid', 'minOccurs': '0', 'type': 'string'}, 'Asset': {'maxOccurs': 'unbounded', 'native': False, 'name': 'asset', 'minOccurs': '0', 'type': 'Asset'}, 'tags': {'native': True, 'name': 'tags', 'minOccurs': '0', 'type': 'string'}, 'Assetlist': {'maxOccurs': 'unbounded', 'native': False, 'name': 'assetlist', 'minOccurs': '0', 'type': 'Assetlist'}, 'assetProperties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'assetproperties', 'minOccurs': '0', 'type': 'AssetProperty'}, 'lifecycleState': {'native': True, 'name': 'lifecyclestate', 'minOccurs': '0', 'type': 'string'}, 'assetPath': {'native': True, 'name': 'assetpath', 'minOccurs': '0', 'type': 'string'}, 'id': {'native': True, 'name': 'id', 'minOccurs': '0', 'type': 'int'}, 'detailedAssetPath': {'native': True, 'name': 'detailedassetpath', 'minOccurs': '0', 'type': 'string'}, 'top': {'native': True, 'name': 'top', 'type': 'boolean'}, 'importMode': {'native': False, 'name': 'importmode', 'minOccurs': '0', 'type': 'ImportMode'}, 'removable': {'native': True, 'name': 'removable', 'minOccurs': '0', 'type': 'boolean'}, 'assetType': {'native': False, 'name': 'assettype', 'minOccurs': '0', 'type': 'Link'}, 'description': {'native': True, 'name': 'description', 'minOccurs': '0', 'type': 'string'}, 'usedByAssets': {'maxOccurs': 'unbounded', 'native': False, 'name': 'usedbyassets', 'minOccurs': '0', 'type': 'Link'}, 'foreignAssetProperties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'foreignassetproperties', 'minOccurs': '0', 'type': 'ForeignAssetProperty'}, 'lifecycleLastComment': {'native': True, 'name': 'lifecyclelastcomment', 'minOccurs': '0', 'type': 'string'}, 'applicationType': {'native': True, 'name': 'applicationtype', 'minOccurs': '0', 'type': 'string'}, 'importDirectives': {'native': False, 'name': 'importdirectives', 'minOccurs': '0', 'type': 'ImportDirectives'}})
        self.lifecycleversion = lifecycleversion
        self.uuid = uuid
        self.asset = asset
        self.tags = tags
        self.assetlist = assetlist
        self.assetproperties = assetproperties
        self.lifecyclestate = lifecyclestate
        self.assetpath = assetpath
        self.id = id
        self.detailedassetpath = detailedassetpath
        self.top = top
        self.removable = removable
        self.assettype = assettype
        self.description = description
        self.usedbyassets = usedbyassets
        self.importmode = importmode
        self.foreignassetproperties = foreignassetproperties
        self.lifecyclelastcomment = lifecyclelastcomment
        self.applicationtype = applicationtype
        self.importdirectives = importdirectives 
