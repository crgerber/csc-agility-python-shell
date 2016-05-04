from core.agility.common.AgilityModelBase import AgilityModelBase

class ImportFileReportBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, failed=False, failreason='', importassetreports=[], filename=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'failed': {'type': 'boolean', 'name': 'failed', 'native': True}, 'failReason': {'type': 'string', 'name': 'failreason', 'native': True}, 'importAssetReports': {'maxOccurs': 'unbounded', 'type': 'ImportAssetReport', 'name': 'importassetreports', 'minOccurs': '0', 'native': False}, 'filename': {'type': 'string', 'name': 'filename', 'native': True}})
        self.failed = failed
        self.failreason = failreason
        self.importassetreports = importassetreports
        self.filename = filename 
