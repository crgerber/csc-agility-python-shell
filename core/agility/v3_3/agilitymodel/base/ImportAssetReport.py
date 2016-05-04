from core.agility.common.AgilityModelBase import AgilityModelBase

class ImportAssetReportBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, assettype='', assetid=None, assetversion='', operationstatus='', assetname='', operation=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'assetType': {'type': 'string', 'name': 'assettype', 'native': True}, 'assetId': {'type': 'int', 'name': 'assetid', 'native': True}, 'assetVersion': {'type': 'string', 'name': 'assetversion', 'native': True}, 'operationStatus': {'type': 'string', 'name': 'operationstatus', 'native': True}, 'assetName': {'type': 'string', 'name': 'assetname', 'native': True}, 'operation': {'type': 'string', 'name': 'operation', 'native': True}})
        self.assettype = assettype
        self.assetid = assetid
        self.assetversion = assetversion
        self.operationstatus = operationstatus
        self.assetname = assetname
        self.operation = operation 
