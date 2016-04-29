from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class RatingBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, createdon=None, user=None, rating=None, updatedon=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'createdOn': {'native': True, 'name': 'createdon', 'minOccurs': '0', 'type': 'date'}, 'user': {'native': False, 'name': 'user', 'minOccurs': '0', 'type': 'Link'}, 'rating': {'native': True, 'name': 'rating', 'type': 'int'}, 'updatedOn': {'native': True, 'name': 'updatedon', 'minOccurs': '0', 'type': 'date'}})
        self.createdon = createdon
        self.user = user
        self.rating = rating
        self.updatedon = updatedon 
