from core.agility.v3_3.agilitymodel.base.OperatingSystem import OperatingSystemBase
from core.agility.v3_3.agilitymodel.actions.OperatingSystem import OperatingSystemActions

class OperatingSystem(OperatingSystemBase, OperatingSystemActions):
    '''
    classdocs
    '''
    def __init__(self, operatingsystemtype=None, effectivefilesystems=[], parentoperatingsystem=None, filesystems=[], displayname=None, mgmtscriptgroup=None):
        '''
        Constructor
        @param operatingsystemtype: operatingsystemtype minOccurs=0
        @type operatingsystemtype: OperatingSystemType
        @param effectivefilesystems: effectivefilesystems minOccurs=0 maxOccurs=unbounded
        @type effectivefilesystems: FileSystem
        @param parentoperatingsystem: parentoperatingsystem
        @type parentoperatingsystem: Link
        @param filesystems: filesystems minOccurs=0 maxOccurs=unbounded
        @type filesystems: FileSystem
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param mgmtscriptgroup: mgmtscriptgroup
        @type mgmtscriptgroup: Link
        '''
        OperatingSystemBase.__init__(self, operatingsystemtype=operatingsystemtype, effectivefilesystems=effectivefilesystems, parentoperatingsystem=parentoperatingsystem, filesystems=filesystems, displayname=displayname, mgmtscriptgroup=mgmtscriptgroup)
