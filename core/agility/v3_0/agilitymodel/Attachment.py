from core.agility.v3_0.agilitymodel.base.Attachment import AttachmentBase
from core.agility.v3_0.agilitymodel.actions.Attachment import AttachmentActions

class Attachment(AttachmentBase, AttachmentActions):
    '''
    classdocs
    '''
    def __init__(self, content=None, attachmentlocation=[], size=None):
        '''
        Constructor
        @param content: content minOccurs=0
        @type content: base64Binary
        @param attachmentlocation: attachmentlocation minOccurs=0 maxOccurs=unbounded
        @type attachmentlocation: AttachmentLocation
        @param size: size minOccurs=0
        @type size: long
        '''
        AttachmentBase.__init__(self, content=content, attachmentlocation=attachmentlocation, size=size)
