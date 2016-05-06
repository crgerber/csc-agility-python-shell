from core.agility.v3_3.agilitymodel.base.PublishRequest import PublishRequestBase
from core.agility.v3_3.agilitymodel.actions.PublishRequest import PublishRequestActions

class PublishRequest(PublishRequestBase, PublishRequestActions):
    '''
    classdocs
    '''
    def __init__(self, comment=None, keepsubassetslocation=None):
        '''
        Constructor
        @param comment: comment minOccurs=0
        @type comment: string
        @param keepsubassetslocation: keepsubassetslocation minOccurs=0
        @type keepsubassetslocation: boolean
        '''
        PublishRequestBase.__init__(self, comment=comment, keepsubassetslocation=keepsubassetslocation)
