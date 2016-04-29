from core.agility.common.AgilityModelBase import AgilityModelBase

class ImportFileReportBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, filename='', importassetreports=[], failed=False, failreason=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'filename': {'native': True, 'name': 'filename', 'type': 'string'}, 'importAssetReports': {'maxOccurs': 'unbounded', 'native': False, 'name': 'importassetreports', 'minOccurs': '0', 'type': 'ImportAssetReport'}, 'failed': {'native': True, 'name': 'failed', 'type': 'boolean'}, 'failReason': {'native': True, 'name': 'failreason', 'type': 'string'}})
        self.filename = filename
        self.importassetreports = importassetreports
        self.failed = failed
        self.failreason = failreason 
