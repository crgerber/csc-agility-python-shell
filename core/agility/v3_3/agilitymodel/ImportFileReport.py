from core.agility.v3_3.agilitymodel.base.ImportFileReport import ImportFileReportBase
from core.agility.v3_3.agilitymodel.actions.ImportFileReport import ImportFileReportActions

class ImportFileReport(ImportFileReportBase, ImportFileReportActions):
    '''
    classdocs
    '''
    def __init__(self, filename='', failreason='', importassetreports=[], failed=False):
        '''
        Constructor
        @param filename: filename
        @type filename: string
        @param failreason: failreason
        @type failreason: string
        @param importassetreports: importassetreports minOccurs=0 maxOccurs=unbounded
        @type importassetreports: ImportAssetReport
        @param failed: failed
        @type failed: boolean
        '''
        ImportFileReportBase.__init__(self, filename=filename, failreason=failreason, importassetreports=importassetreports, failed=failed)
