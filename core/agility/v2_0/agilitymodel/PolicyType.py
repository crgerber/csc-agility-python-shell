from core.agility.v2_0.agilitymodel.base.PolicyType import PolicyTypeBase
from core.agility.v2_0.agilitymodel.actions.PolicyType import PolicyTypeActions

class PolicyType(PolicyTypeBase, PolicyTypeActions):
    '''
    classdocs
    '''
    def __init__(self, bundleVersion='', symbolicName=''):
        '''
        Constructor
        @param bundleVersion: bundleVersion
        @type bundleVersion: string
        @param symbolicName: symbolicName
        @type symbolicName: string
        '''
        PolicyTypeBase.__init__(self, bundleVersion=bundleVersion, symbolicName=symbolicName)
