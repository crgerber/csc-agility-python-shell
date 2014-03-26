from core.agility.v3_0.agilitymodel.base.ArtifactAttachment import ArtifactAttachmentBase
from core.agility.v3_0.agilitymodel.actions.ArtifactAttachment import ArtifactAttachmentActions

class ArtifactAttachment(ArtifactAttachmentBase, ArtifactAttachmentActions):
    '''
    classdocs
    '''
    def __init__(self, content=None, artifact=None, size=None):
        '''
        Constructor
        @param content: content minOccurs=0
        @type content: base64Binary
        @param artifact: artifact minOccurs=0
        @type artifact: Link
        @param size: size minOccurs=0
        @type size: long
        '''
        ArtifactAttachmentBase.__init__(self, content=content, artifact=artifact, size=size)
