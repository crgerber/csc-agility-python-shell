from core.agility.v3_3.agilitymodel.base.Rating import RatingBase
from core.agility.v3_3.agilitymodel.actions.Rating import RatingActions

class Rating(RatingBase, RatingActions):
    '''
    classdocs
    '''
    def __init__(self, createdon=None, user=None, rating=None, updatedon=None):
        '''
        Constructor
        @param createdon: createdon minOccurs=0
        @type createdon: date
        @param user: user minOccurs=0
        @type user: Link
        @param rating: rating
        @type rating: int
        @param updatedon: updatedon minOccurs=0
        @type updatedon: date
        '''
        RatingBase.__init__(self, createdon=createdon, user=user, rating=rating, updatedon=updatedon)
