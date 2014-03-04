from core.restclient.v2_0.agilitymodel.base.Attachment import AttachmentBase
from core.restclient.v2_0.agilitymodel.actions.Attachment import AttachmentActions

class Attachment(AttachmentBase, AttachmentActions):
    '''
    classdocs
    '''
    def __init__(self, content=None, attachmentLocation=list(), size=None):
        '''
        Constructor
        @param content: content minOccurs=0
        @type content: base64Binary
        @param attachmentLocation: attachmentLocation minOccurs=0 maxOccurs=unbounded
        @type attachmentLocation: AttachmentLocation
        @param size: size minOccurs=0
        @type size: long
        '''
        AttachmentBase.__init__(self, content=content, attachmentLocation=attachmentLocation, size=size)
