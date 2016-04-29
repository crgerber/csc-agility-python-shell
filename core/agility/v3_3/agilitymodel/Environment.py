from core.agility.v3_3.agilitymodel.base.Environment import EnvironmentBase
from core.agility.v3_3.agilitymodel.actions.Environment import EnvironmentActions

class Environment(EnvironmentBase, EnvironmentActions):
    '''
    classdocs
    '''
    def __init__(self, private=False, deployments=[], runtimes=[], type=None):
        '''
        Constructor
        @param private: private
        @type private: boolean
        @param deployments: deployments minOccurs=0 maxOccurs=unbounded
        @type deployments: Link
        @param runtimes: runtimes minOccurs=0 maxOccurs=unbounded
        @type runtimes: Link
        @param type: type minOccurs=0
        @type type: Link
        '''
        EnvironmentBase.__init__(self, private=private, deployments=deployments, runtimes=runtimes, type=type)
