from core.agility.common.AgilityModelBase import AgilityModelBase

class ImportReportBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, importfilereports=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'importFileReports': {'maxOccurs': 'unbounded', 'type': 'ImportFileReport', 'name': 'importfilereports', 'minOccurs': '0', 'native': False}})
        self.importfilereports = importfilereports 
