from core.agility.v3_3.agilitymodel.base.PolicyType import PolicyTypeBase
from core.agility.v3_3.agilitymodel.actions.PolicyType import PolicyTypeActions

class PolicyType(PolicyTypeBase, PolicyTypeActions):
    '''
    classdocs
    '''
    def __init__(self, symbolicname='', bundleversion=''):
        '''
        Constructor
        @param symbolicname: symbolicname
        @type symbolicname: string
        @param bundleversion: bundleversion
        @type bundleversion: string
        '''
        PolicyTypeBase.__init__(self, symbolicname=symbolicname, bundleversion=bundleversion)
