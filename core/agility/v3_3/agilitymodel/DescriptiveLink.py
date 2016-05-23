from core.agility.v3_3.agilitymodel.base.DescriptiveLink import DescriptiveLinkBase
from core.agility.v3_3.agilitymodel.actions.DescriptiveLink import DescriptiveLinkActions

class DescriptiveLink(DescriptiveLinkBase, DescriptiveLinkActions):
    '''
    classdocs
    '''
    def __init__(self, description=None, displayname=None):
        '''
        Constructor
        @param description: description minOccurs=0
        @type description: string
        @param displayname: displayname minOccurs=0
        @type displayname: string
        '''
        DescriptiveLinkBase.__init__(self, description=description, displayname=displayname)
