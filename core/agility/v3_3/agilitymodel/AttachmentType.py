from core.agility.v3_3.agilitymodel.base.AttachmentType import AttachmentTypeBase
from core.agility.v3_3.agilitymodel.actions.AttachmentType import AttachmentTypeActions

class AttachmentType(AttachmentTypeBase, AttachmentTypeActions):
    '''
    classdocs
    '''
    def __init__(self, vpcid=None, state=None):
        '''
        Constructor
        @param vpcid: vpcid minOccurs=0
        @type vpcid: string
        @param state: state minOccurs=0
        @type state: string
        '''
        AttachmentTypeBase.__init__(self, vpcid=vpcid, state=state)
