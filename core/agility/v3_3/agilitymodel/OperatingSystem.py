from base.OperatingSystem import OperatingSystemBase
from actions.OperatingSystem import OperatingSystemActions

class OperatingSystem(OperatingSystemBase, OperatingSystemActions):
    '''
    classdocs
    '''
    def __init__(self, displayname=None, parentoperatingsystem=None, mgmtscriptgroup=None, filesystems=[], operatingsystemtype=None, effectivefilesystems=[]):
        '''
        Constructor
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param parentoperatingsystem: parentoperatingsystem
        @type parentoperatingsystem: Link
        @param mgmtscriptgroup: mgmtscriptgroup
        @type mgmtscriptgroup: Link
        @param filesystems: filesystems minOccurs=0 maxOccurs=unbounded
        @type filesystems: FileSystem
        @param operatingsystemtype: operatingsystemtype minOccurs=0
        @type operatingsystemtype: OperatingSystemType
        @param effectivefilesystems: effectivefilesystems minOccurs=0 maxOccurs=unbounded
        @type effectivefilesystems: FileSystem
        '''
        OperatingSystemBase.__init__(self, displayname=displayname, parentoperatingsystem=parentoperatingsystem, mgmtscriptgroup=mgmtscriptgroup, filesystems=filesystems, operatingsystemtype=operatingsystemtype, effectivefilesystems=effectivefilesystems)
