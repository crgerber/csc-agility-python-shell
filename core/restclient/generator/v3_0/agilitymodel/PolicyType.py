from .base.PolicyType import PolicyTypeBase
from .actions.PolicyType import PolicyTypeActions

class PolicyType(PolicyTypeBase, PolicyTypeActions):
    '''
    classdocs
    '''
    def __init__(self, bundleversion='', symbolicname=''):
        '''
        Constructor
        @param bundleversion: bundleversion
        @type bundleversion: string
        @param symbolicname: symbolicname
        @type symbolicname: string
        '''
        PolicyTypeBase.__init__(self, bundleversion=bundleversion, symbolicname=symbolicname)
