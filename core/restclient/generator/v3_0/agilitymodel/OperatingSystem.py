from .base.OperatingSystem import OperatingSystemBase
from .actions.OperatingSystem import OperatingSystemActions

class OperatingSystem(OperatingSystemBase, OperatingSystemActions):
    '''
    classdocs
    '''
    def __init__(self, mgmtscriptgroup=None, displayname=None, effectivefilesystems=[], filesystems=[]):
        '''
        Constructor
        @param mgmtscriptgroup: mgmtscriptgroup
        @type mgmtscriptgroup: Link
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param effectivefilesystems: effectivefilesystems minOccurs=0 maxOccurs=unbounded
        @type effectivefilesystems: FileSystem
        @param filesystems: filesystems minOccurs=0 maxOccurs=unbounded
        @type filesystems: FileSystem
        '''
        OperatingSystemBase.__init__(self, mgmtscriptgroup=mgmtscriptgroup, displayname=displayname, effectivefilesystems=effectivefilesystems, filesystems=filesystems)
