from core.agility.common.AgilityModelBase import AgilityModelBase

class ImportFileReportBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, filename='', failreason='', importassetreports=[], failed=False):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'filename': {'name': 'filename', 'native': True, 'type': 'string'}, 'failed': {'name': 'failed', 'native': True, 'type': 'boolean'}, 'importAssetReports': {'name': 'importassetreports', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'ImportAssetReport'}, 'failReason': {'name': 'failreason', 'native': True, 'type': 'string'}})
        self.filename = filename
        self.failreason = failreason
        self.importassetreports = importassetreports
        self.failed = failed 
