from core.agility.v3_3.agilitymodel.base.Comment import CommentBase
from core.agility.v3_3.agilitymodel.actions.Comment import CommentActions

class Comment(CommentBase, CommentActions):
    '''
    classdocs
    '''
    def __init__(self, user=None, comment=None, createdon=None, updatedon=None):
        '''
        Constructor
        @param user: user minOccurs=0
        @type user: Link
        @param comment: comment minOccurs=0
        @type comment: string
        @param createdon: createdon minOccurs=0
        @type createdon: date
        @param updatedon: updatedon minOccurs=0
        @type updatedon: date
        '''
        CommentBase.__init__(self, user=user, comment=comment, createdon=createdon, updatedon=updatedon)
