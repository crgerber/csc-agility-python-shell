from base.Environment import EnvironmentBase
from actions.Environment import EnvironmentActions

class Environment(EnvironmentBase, EnvironmentActions):
    '''
    classdocs
    '''
    def __init__(self, runtimes=[], type=None, private=False, deployments=[]):
        '''
        Constructor
        @param runtimes: runtimes minOccurs=0 maxOccurs=unbounded
        @type runtimes: Link
        @param type: type minOccurs=0
        @type type: Link
        @param private: private
        @type private: boolean
        @param deployments: deployments minOccurs=0 maxOccurs=unbounded
        @type deployments: Link
        '''
        EnvironmentBase.__init__(self, runtimes=runtimes, type=type, private=private, deployments=deployments)
