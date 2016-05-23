from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class RatingBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, createdon=None, user=None, rating=None, updatedon=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'createdOn': {'name': 'createdon', 'minOccurs': '0', 'native': True, 'type': 'date'}, 'user': {'name': 'user', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'updatedOn': {'name': 'updatedon', 'minOccurs': '0', 'native': True, 'type': 'date'}, 'rating': {'name': 'rating', 'native': True, 'type': 'int'}})
        self.createdon = createdon
        self.user = user
        self.rating = rating
        self.updatedon = updatedon 
