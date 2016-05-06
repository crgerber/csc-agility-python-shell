from core.agility.v3_3.agilitymodel.base.AttachmentType import AttachmentTypeBase
from core.agility.v3_3.agilitymodel.actions.AttachmentType import AttachmentTypeActions

class AttachmentType(AttachmentTypeBase, AttachmentTypeActions):
    '''
    classdocs
    '''
    def __init__(self, state=None, vpcid=None):
        '''
        Constructor
        @param state: state minOccurs=0
        @type state: string
        @param vpcid: vpcid minOccurs=0
        @type vpcid: string
        '''
        AttachmentTypeBase.__init__(self, state=state, vpcid=vpcid)
