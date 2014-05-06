from core.agility.v2_0.agilitymodel.base.Environment import EnvironmentBase
from core.agility.v2_0.agilitymodel.actions.Environment import EnvironmentActions

class Environment(EnvironmentBase, EnvironmentActions):
    '''
    classdocs
    '''
    def __init__(self, runtimes=list(), type=None, private=False, deployments=list()):
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
