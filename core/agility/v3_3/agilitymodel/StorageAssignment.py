from core.agility.v3_3.agilitymodel.base.StorageAssignment import StorageAssignmentBase
from core.agility.v3_3.agilitymodel.actions.StorageAssignment import StorageAssignmentActions

class StorageAssignment(StorageAssignmentBase, StorageAssignmentActions):
    '''
    classdocs
    '''
    def __init__(self, attachtime=None, device=None, instanceid=None, status=None):
        '''
        Constructor
        @param attachtime: attachtime minOccurs=0
        @type attachtime: dateTime
        @param device: device minOccurs=0
        @type device: string
        @param instanceid: instanceid minOccurs=0
        @type instanceid: string
        @param status: status minOccurs=0
        @type status: string
        '''
        StorageAssignmentBase.__init__(self, attachtime=attachtime, device=device, instanceid=instanceid, status=status)
