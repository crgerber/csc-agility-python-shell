from core.agility.v3_3.agilitymodel.base.OperatingSystem import OperatingSystemBase
from core.agility.v3_3.agilitymodel.actions.OperatingSystem import OperatingSystemActions

class OperatingSystem(OperatingSystemBase, OperatingSystemActions):
    '''
    classdocs
    '''
    def __init__(self, operatingsystemtype=None, displayname=None, parentoperatingsystem=None, effectivefilesystems=[], filesystems=[], mgmtscriptgroup=None):
        '''
        Constructor
        @param operatingsystemtype: operatingsystemtype minOccurs=0
        @type operatingsystemtype: OperatingSystemType
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param parentoperatingsystem: parentoperatingsystem
        @type parentoperatingsystem: Link
        @param effectivefilesystems: effectivefilesystems minOccurs=0 maxOccurs=unbounded
        @type effectivefilesystems: FileSystem
        @param filesystems: filesystems minOccurs=0 maxOccurs=unbounded
        @type filesystems: FileSystem
        @param mgmtscriptgroup: mgmtscriptgroup
        @type mgmtscriptgroup: Link
        '''
        OperatingSystemBase.__init__(self, operatingsystemtype=operatingsystemtype, displayname=displayname, parentoperatingsystem=parentoperatingsystem, effectivefilesystems=effectivefilesystems, filesystems=filesystems, mgmtscriptgroup=mgmtscriptgroup)
