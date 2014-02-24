from base.Comment import CommentBase
from actions.Comment import CommentActions

class Comment(CommentBase, CommentActions):
    '''
    classdocs
    '''
    def __init__(self, comment=None, createdOn=None, user=None, updatedOn=None):
        '''
        Constructor
        @param comment: comment minOccurs=0
        @type comment: string
        @param createdOn: createdOn minOccurs=0
        @type createdOn: date
        @param user: user minOccurs=0
        @type user: Link
        @param updatedOn: updatedOn minOccurs=0
        @type updatedOn: date
        '''
        CommentBase.__init__(self, comment=comment, createdOn=createdOn, user=user, updatedOn=updatedOn)
