from base.AccessUri import AccessUriBase
from actions.AccessUri import AccessUriActions

class AccessUri(AccessUriBase, AccessUriActions):
    '''
    classdocs
    '''
    def __init__(self, type=None, accessuri=None, accessuriexpanded=None, label=None):
        '''
        Constructor
        @param type: type minOccurs=0
        @type type: int
        @param accessuri: accessuri minOccurs=0
        @type accessuri: string
        @param accessuriexpanded: accessuriexpanded minOccurs=0
        @type accessuriexpanded: string
        @param label: label minOccurs=0
        @type label: string
        '''
        AccessUriBase.__init__(self, type=type, accessuri=accessuri, accessuriexpanded=accessuriexpanded, label=label)
