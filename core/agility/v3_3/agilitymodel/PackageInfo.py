from core.agility.v3_3.agilitymodel.base.PackageInfo import PackageInfoBase
from core.agility.v3_3.agilitymodel.actions.PackageInfo import PackageInfoActions

class PackageInfo(PackageInfoBase, PackageInfoActions):
    '''
    classdocs
    '''
    def __init__(self, name='', version=''):
        '''
        Constructor
        @param name: name
        @type name: string
        @param version: version
        @type version: string
        '''
        PackageInfoBase.__init__(self, name=name, version=version)
