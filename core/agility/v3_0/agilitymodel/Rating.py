from core.agility.v3_0.agilitymodel.base.Rating import RatingBase
from core.agility.v3_0.agilitymodel.actions.Rating import RatingActions

class Rating(RatingBase, RatingActions):
    '''
    classdocs
    '''
    def __init__(self, rating=None, createdon=None, user=None, updatedon=None):
        '''
        Constructor
        @param rating: rating
        @type rating: int
        @param createdon: createdon minOccurs=0
        @type createdon: date
        @param user: user minOccurs=0
        @type user: Link
        @param updatedon: updatedon minOccurs=0
        @type updatedon: date
        '''
        RatingBase.__init__(self, rating=rating, createdon=createdon, user=user, updatedon=updatedon)
