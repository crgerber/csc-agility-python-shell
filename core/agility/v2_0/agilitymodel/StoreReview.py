from core.agility.v2_0.agilitymodel.base.StoreReview import StoreReviewBase
from core.agility.v2_0.agilitymodel.actions.StoreReview import StoreReviewActions

class StoreReview(StoreReviewBase, StoreReviewActions):
    '''
    classdocs
    '''
    def __init__(self, userName=None, rating=None, title=None, createdOn=None, updatedOn=None, userId=None, comment=None, productId=None):
        '''
        Constructor
        @param userName: userName minOccurs=0
        @type userName: string
        @param rating: rating minOccurs=0
        @type rating: int
        @param title: title minOccurs=0
        @type title: string
        @param createdOn: createdOn minOccurs=0
        @type createdOn: date
        @param updatedOn: updatedOn minOccurs=0
        @type updatedOn: date
        @param userId: userId minOccurs=0
        @type userId: int
        @param comment: comment minOccurs=0
        @type comment: string
        @param productId: productId minOccurs=0
        @type productId: int
        '''
        StoreReviewBase.__init__(self, userName=userName, rating=rating, title=title, createdOn=createdOn, updatedOn=updatedOn, userId=userId, comment=comment, productId=productId)
