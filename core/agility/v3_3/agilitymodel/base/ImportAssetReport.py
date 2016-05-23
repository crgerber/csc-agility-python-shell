from core.agility.common.AgilityModelBase import AgilityModelBase

class ImportAssetReportBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, assettype='', assetid=None, assetname='', assetversion='', operation='', operationstatus=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'assetType': {'name': 'assettype', 'native': True, 'type': 'string'}, 'assetId': {'name': 'assetid', 'native': True, 'type': 'int'}, 'assetName': {'name': 'assetname', 'native': True, 'type': 'string'}, 'assetVersion': {'name': 'assetversion', 'native': True, 'type': 'string'}, 'operation': {'name': 'operation', 'native': True, 'type': 'string'}, 'operationStatus': {'name': 'operationstatus', 'native': True, 'type': 'string'}})
        self.assettype = assettype
        self.assetid = assetid
        self.assetname = assetname
        self.assetversion = assetversion
        self.operation = operation
        self.operationstatus = operationstatus 
