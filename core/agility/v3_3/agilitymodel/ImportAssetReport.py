from core.agility.v3_3.agilitymodel.base.ImportAssetReport import ImportAssetReportBase
from core.agility.v3_3.agilitymodel.actions.ImportAssetReport import ImportAssetReportActions

class ImportAssetReport(ImportAssetReportBase, ImportAssetReportActions):
    '''
    classdocs
    '''
    def __init__(self, assettype='', assetid=None, assetname='', assetversion='', operation='', operationstatus=''):
        '''
        Constructor
        @param assettype: assettype
        @type assettype: string
        @param assetid: assetid
        @type assetid: int
        @param assetname: assetname
        @type assetname: string
        @param assetversion: assetversion
        @type assetversion: string
        @param operation: operation
        @type operation: string
        @param operationstatus: operationstatus
        @type operationstatus: string
        '''
        ImportAssetReportBase.__init__(self, assettype=assettype, assetid=assetid, assetname=assetname, assetversion=assetversion, operation=operation, operationstatus=operationstatus)
