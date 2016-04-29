from core.agility.v3_3.agilitymodel.base.ImportAssetReport import ImportAssetReportBase
from core.agility.v3_3.agilitymodel.actions.ImportAssetReport import ImportAssetReportActions

class ImportAssetReport(ImportAssetReportBase, ImportAssetReportActions):
    '''
    classdocs
    '''
    def __init__(self, assetversion='', operationstatus='', assetid=None, assettype='', operation='', assetname=''):
        '''
        Constructor
        @param assetversion: assetversion
        @type assetversion: string
        @param operationstatus: operationstatus
        @type operationstatus: string
        @param assetid: assetid
        @type assetid: int
        @param assettype: assettype
        @type assettype: string
        @param operation: operation
        @type operation: string
        @param assetname: assetname
        @type assetname: string
        '''
        ImportAssetReportBase.__init__(self, assetversion=assetversion, operationstatus=operationstatus, assetid=assetid, assettype=assettype, operation=operation, assetname=assetname)
