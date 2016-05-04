from base.InstanceVariableRequest import InstanceVariableRequestBase
from actions.InstanceVariableRequest import InstanceVariableRequestActions

class InstanceVariableRequest(InstanceVariableRequestBase, InstanceVariableRequestActions):
    '''
    classdocs
    '''
    def __init__(self, instanceid=None):
        '''
        Constructor
        @param instanceid: instanceid
        @type instanceid: int
        '''
        InstanceVariableRequestBase.__init__(self, instanceid=instanceid)
