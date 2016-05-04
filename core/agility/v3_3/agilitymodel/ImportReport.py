from base.ImportReport import ImportReportBase
from actions.ImportReport import ImportReportActions

class ImportReport(ImportReportBase, ImportReportActions):
    '''
    classdocs
    '''
    def __init__(self, importfilereports=[]):
        '''
        Constructor
        @param importfilereports: importfilereports minOccurs=0 maxOccurs=unbounded
        @type importfilereports: ImportFileReport
        '''
        ImportReportBase.__init__(self, importfilereports=importfilereports)
