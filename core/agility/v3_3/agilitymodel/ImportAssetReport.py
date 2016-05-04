from core.agility.v3_3.agilitymodel.base.ImportAssetReport import ImportAssetReportBase
from core.agility.v3_3.agilitymodel.actions.ImportAssetReport import ImportAssetReportActions

class ImportAssetReport(ImportAssetReportBase, ImportAssetReportActions):
    '''
    classdocs
    '''
    def __init__(self, assettype='', assetid=None, assetversion='', operationstatus='', assetname='', operation=''):
        '''
        Constructor
        @param assettype: assettype
        @type assettype: string
        @param assetid: assetid
        @type assetid: int
        @param assetversion: assetversion
        @type assetversion: string
        @param operationstatus: operationstatus
        @type operationstatus: string
        @param assetname: assetname
        @type assetname: string
        @param operation: operation
        @type operation: string
        '''
        ImportAssetReportBase.__init__(self, assettype=assettype, assetid=assetid, assetversion=assetversion, operationstatus=operationstatus, assetname=assetname, operation=operation)
