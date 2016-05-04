from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class RatingBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, rating=None, createdon=None, user=None, updatedon=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'rating': {'type': 'int', 'name': 'rating', 'native': True}, 'createdOn': {'type': 'date', 'name': 'createdon', 'minOccurs': '0', 'native': True}, 'user': {'type': 'Link', 'name': 'user', 'minOccurs': '0', 'native': False}, 'updatedOn': {'type': 'date', 'name': 'updatedon', 'minOccurs': '0', 'native': True}})
        self.rating = rating
        self.createdon = createdon
        self.user = user
        self.updatedon = updatedon 
