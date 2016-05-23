from core.agility.v3_3.agilitymodel.base.AccessUri import AccessUriBase
from core.agility.v3_3.agilitymodel.actions.AccessUri import AccessUriActions

class AccessUri(AccessUriBase, AccessUriActions):
    '''
    classdocs
    '''
    def __init__(self, accessuriexpanded=None, accessuri=None, label=None, type=None):
        '''
        Constructor
        @param accessuriexpanded: accessuriexpanded minOccurs=0
        @type accessuriexpanded: string
        @param accessuri: accessuri minOccurs=0
        @type accessuri: string
        @param label: label minOccurs=0
        @type label: string
        @param type: type minOccurs=0
        @type type: int
        '''
        AccessUriBase.__init__(self, accessuriexpanded=accessuriexpanded, accessuri=accessuri, label=label, type=type)
