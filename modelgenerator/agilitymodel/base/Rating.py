from Asset import AssetBase

class RatingBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, rating=None, createdOn=None, user=None, updatedOn=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'rating': {'type': 'int', 'name': 'rating', 'native': True}, 'createdOn': {'type': 'date', 'name': 'createdOn', 'minOccurs': '0', 'native': True}, 'user': {'type': 'Link', 'name': 'user', 'minOccurs': '0', 'native': False}, 'updatedOn': {'type': 'date', 'name': 'updatedOn', 'minOccurs': '0', 'native': True}})
        self.rating = rating
        self.createdOn = createdOn
        self.user = user
        self.updatedOn = updatedOn 
