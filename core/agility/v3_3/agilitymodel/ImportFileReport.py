from core.agility.v3_3.agilitymodel.base.ImportFileReport import ImportFileReportBase
from core.agility.v3_3.agilitymodel.actions.ImportFileReport import ImportFileReportActions

class ImportFileReport(ImportFileReportBase, ImportFileReportActions):
    '''
    classdocs
    '''
    def __init__(self, filename='', importassetreports=[], failed=False, failreason=''):
        '''
        Constructor
        @param filename: filename
        @type filename: string
        @param importassetreports: importassetreports minOccurs=0 maxOccurs=unbounded
        @type importassetreports: ImportAssetReport
        @param failed: failed
        @type failed: boolean
        @param failreason: failreason
        @type failreason: string
        '''
        ImportFileReportBase.__init__(self, filename=filename, importassetreports=importassetreports, failed=failed, failreason=failreason)
