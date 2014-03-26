from core.agility.v2_0.agilitymodel.base.OperatingSystem import OperatingSystemBase
from core.agility.v2_0.agilitymodel.actions.OperatingSystem import OperatingSystemActions

class OperatingSystem(OperatingSystemBase, OperatingSystemActions):
    '''
    classdocs
    '''
    def __init__(self, displayName=None, effectiveFileSystems=list(), fileSystems=list()):
        '''
        Constructor
        @param displayName: displayName minOccurs=0
        @type displayName: string
        @param effectiveFileSystems: effectiveFileSystems minOccurs=0 maxOccurs=unbounded
        @type effectiveFileSystems: FileSystem
        @param fileSystems: fileSystems minOccurs=0 maxOccurs=unbounded
        @type fileSystems: FileSystem
        '''
        OperatingSystemBase.__init__(self, displayName=displayName, effectiveFileSystems=effectiveFileSystems, fileSystems=fileSystems)
