from .base.DescriptiveLink import DescriptiveLinkBase
from .actions.DescriptiveLink import DescriptiveLinkActions

class DescriptiveLink(DescriptiveLinkBase, DescriptiveLinkActions):
    '''
    classdocs
    '''
    def __init__(self, displayname=None, description=None):
        '''
        Constructor
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param description: description minOccurs=0
        @type description: string
        '''
        DescriptiveLinkBase.__init__(self, displayname=displayname, description=description)
