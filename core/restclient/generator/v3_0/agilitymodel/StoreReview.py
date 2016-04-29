from .base.StoreReview import StoreReviewBase
from .actions.StoreReview import StoreReviewActions

class StoreReview(StoreReviewBase, StoreReviewActions):
    '''
    classdocs
    '''
    def __init__(self, username=None, rating=None, title=None, createdon=None, updatedon=None, userid=None, comment=None, productid=None):
        '''
        Constructor
        @param username: username minOccurs=0
        @type username: string
        @param rating: rating minOccurs=0
        @type rating: int
        @param title: title minOccurs=0
        @type title: string
        @param createdon: createdon minOccurs=0
        @type createdon: date
        @param updatedon: updatedon minOccurs=0
        @type updatedon: date
        @param userid: userid minOccurs=0
        @type userid: int
        @param comment: comment minOccurs=0
        @type comment: string
        @param productid: productid minOccurs=0
        @type productid: int
        '''
        StoreReviewBase.__init__(self, username=username, rating=rating, title=title, createdon=createdon, updatedon=updatedon, userid=userid, comment=comment, productid=productid)
