from core.agility.common.AgilityModelBase import AgilityModelBase

class ImportReportBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, importfilereports=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'importFileReports': {'name': 'importfilereports', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'ImportFileReport'}})
        self.importfilereports = importfilereports 
