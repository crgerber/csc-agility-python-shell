from core.agility.v3_3.agilitymodel.base.VersionList import VersionListBase
from core.agility.v3_3.agilitymodel.actions.VersionList import VersionListActions

class VersionList(VersionListBase, VersionListActions):
    '''
    classdocs
    '''
    def __init__(self, versions=[]):
        '''
        Constructor
        @param versions: versions minOccurs=0 maxOccurs=unbounded
        @type versions: AgilityVersion
        '''
        VersionListBase.__init__(self, versions=versions)
