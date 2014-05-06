from core.agility.v2_0.agilitymodel.base.AccessUri import AccessUriBase
from core.agility.v2_0.agilitymodel.actions.AccessUri import AccessUriActions

class AccessUri(AccessUriBase, AccessUriActions):
    '''
    classdocs
    '''
    def __init__(self, type=None, accessUri=None, accessUriExpanded=None, label=None):
        '''
        Constructor
        @param type: type minOccurs=0
        @type type: int
        @param accessUri: accessUri minOccurs=0
        @type accessUri: string
        @param accessUriExpanded: accessUriExpanded minOccurs=0
        @type accessUriExpanded: string
        @param label: label minOccurs=0
        @type label: string
        '''
        AccessUriBase.__init__(self, type=type, accessUri=accessUri, accessUriExpanded=accessUriExpanded, label=label)
