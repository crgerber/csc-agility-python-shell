from base.StorageAssignment import StorageAssignmentBase
from actions.StorageAssignment import StorageAssignmentActions

class StorageAssignment(StorageAssignmentBase, StorageAssignmentActions):
    '''
    classdocs
    '''
    def __init__(self, instanceid=None, device=None, status=None, attachtime=None):
        '''
        Constructor
        @param instanceid: instanceid minOccurs=0
        @type instanceid: string
        @param device: device minOccurs=0
        @type device: string
        @param status: status minOccurs=0
        @type status: string
        @param attachtime: attachtime minOccurs=0
        @type attachtime: dateTime
        '''
        StorageAssignmentBase.__init__(self, instanceid=instanceid, device=device, status=status, attachtime=attachtime)
