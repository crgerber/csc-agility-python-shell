from core.agility.common.AgilityModelBase import AgilityModelBase

class ImportAssetReportBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, assetversion='', operationstatus='', assetid=None, assettype='', operation='', assetname=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'assetVersion': {'native': True, 'name': 'assetversion', 'type': 'string'}, 'operationStatus': {'native': True, 'name': 'operationstatus', 'type': 'string'}, 'assetId': {'native': True, 'name': 'assetid', 'type': 'int'}, 'assetType': {'native': True, 'name': 'assettype', 'type': 'string'}, 'operation': {'native': True, 'name': 'operation', 'type': 'string'}, 'assetName': {'native': True, 'name': 'assetname', 'type': 'string'}})
        self.assetversion = assetversion
        self.operationstatus = operationstatus
        self.assetid = assetid
        self.assettype = assettype
        self.operation = operation
        self.assetname = assetname 
