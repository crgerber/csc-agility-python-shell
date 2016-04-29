from .base.VersionList import VersionListBase
from .actions.VersionList import VersionListActions

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
