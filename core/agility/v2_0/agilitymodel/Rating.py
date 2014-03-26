from core.agility.v2_0.agilitymodel.base.Rating import RatingBase
from core.agility.v2_0.agilitymodel.actions.Rating import RatingActions

class Rating(RatingBase, RatingActions):
    '''
    classdocs
    '''
    def __init__(self, rating=None, createdOn=None, user=None, updatedOn=None):
        '''
        Constructor
        @param rating: rating
        @type rating: int
        @param createdOn: createdOn minOccurs=0
        @type createdOn: date
        @param user: user minOccurs=0
        @type user: Link
        @param updatedOn: updatedOn minOccurs=0
        @type updatedOn: date
        '''
        RatingBase.__init__(self, rating=rating, createdOn=createdOn, user=user, updatedOn=updatedOn)
