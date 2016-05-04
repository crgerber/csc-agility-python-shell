from base.License import LicenseBase
from actions.License import LicenseActions

class License(LicenseBase, LicenseActions):
    '''
    classdocs
    '''
    def __init__(self, license=''):
        '''
        Constructor
        @param license: license
        @type license: string
        '''
        LicenseBase.__init__(self, license=license)
