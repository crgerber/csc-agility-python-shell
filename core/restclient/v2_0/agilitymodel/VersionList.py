from core.restclient.v2_0.agilitymodel.base.VersionList import VersionListBase
from core.restclient.v2_0.agilitymodel.actions.VersionList import VersionListActions

class VersionList(VersionListBase, VersionListActions):
    '''
    classdocs
    '''
    def __init__(self, versions=list()):
        '''
        Constructor
        @param versions: versions minOccurs=0 maxOccurs=unbounded
        @type versions: AgilityVersion
        '''
        VersionListBase.__init__(self, versions=versions)
