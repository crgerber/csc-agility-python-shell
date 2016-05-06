from core.agility.v3_3.agilitymodel.base.PackageInfo import PackageInfoBase
from core.agility.v3_3.agilitymodel.actions.PackageInfo import PackageInfoActions

class PackageInfo(PackageInfoBase, PackageInfoActions):
    '''
    classdocs
    '''
    def __init__(self, version='', name=''):
        '''
        Constructor
        @param version: version
        @type version: string
        @param name: name
        @type name: string
        '''
        PackageInfoBase.__init__(self, version=version, name=name)
