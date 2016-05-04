from core.agility.v3_3.agilitymodel.base.ImportFileReport import ImportFileReportBase
from core.agility.v3_3.agilitymodel.actions.ImportFileReport import ImportFileReportActions

class ImportFileReport(ImportFileReportBase, ImportFileReportActions):
    '''
    classdocs
    '''
    def __init__(self, failed=False, failreason='', importassetreports=[], filename=''):
        '''
        Constructor
        @param failed: failed
        @type failed: boolean
        @param failreason: failreason
        @type failreason: string
        @param importassetreports: importassetreports minOccurs=0 maxOccurs=unbounded
        @type importassetreports: ImportAssetReport
        @param filename: filename
        @type filename: string
        '''
        ImportFileReportBase.__init__(self, failed=failed, failreason=failreason, importassetreports=importassetreports, filename=filename)
