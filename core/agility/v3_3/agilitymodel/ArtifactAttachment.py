from core.agility.v3_3.agilitymodel.base.ArtifactAttachment import ArtifactAttachmentBase
from core.agility.v3_3.agilitymodel.actions.ArtifactAttachment import ArtifactAttachmentActions

class ArtifactAttachment(ArtifactAttachmentBase, ArtifactAttachmentActions):
    '''
    classdocs
    '''
    def __init__(self, size=None, content=None, artifact=None):
        '''
        Constructor
        @param size: size minOccurs=0
        @type size: long
        @param content: content minOccurs=0
        @type content: base64Binary
        @param artifact: artifact minOccurs=0
        @type artifact: Link
        '''
        ArtifactAttachmentBase.__init__(self, size=size, content=content, artifact=artifact)
