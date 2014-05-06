from core.agility.v3_0.agilitymodel.base.Comment import CommentBase
from core.agility.v3_0.agilitymodel.actions.Comment import CommentActions

class Comment(CommentBase, CommentActions):
    '''
    classdocs
    '''
    def __init__(self, comment=None, createdon=None, user=None, updatedon=None):
        '''
        Constructor
        @param comment: comment minOccurs=0
        @type comment: string
        @param createdon: createdon minOccurs=0
        @type createdon: date
        @param user: user minOccurs=0
        @type user: Link
        @param updatedon: updatedon minOccurs=0
        @type updatedon: date
        '''
        CommentBase.__init__(self, comment=comment, createdon=createdon, user=user, updatedon=updatedon)
