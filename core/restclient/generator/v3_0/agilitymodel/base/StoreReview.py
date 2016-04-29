from .Asset import AssetBase

class StoreReviewBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, username=None, rating=None, title=None, createdon=None, updatedon=None, userid=None, comment=None, productid=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'userName': {'type': 'string', 'name': 'username', 'minOccurs': '0', 'native': True}, 'rating': {'type': 'int', 'name': 'rating', 'minOccurs': '0', 'native': True}, 'updatedOn': {'type': 'date', 'name': 'updatedon', 'minOccurs': '0', 'native': True}, 'createdOn': {'type': 'date', 'name': 'createdon', 'minOccurs': '0', 'native': True}, 'title': {'type': 'string', 'name': 'title', 'minOccurs': '0', 'native': True}, 'userId': {'type': 'int', 'name': 'userid', 'minOccurs': '0', 'native': True}, 'comment': {'type': 'string', 'name': 'comment', 'minOccurs': '0', 'native': True}, 'productId': {'type': 'int', 'name': 'productid', 'minOccurs': '0', 'native': True}})
        self.username = username
        self.rating = rating
        self.title = title
        self.createdon = createdon
        self.updatedon = updatedon
        self.userid = userid
        self.comment = comment
        self.productid = productid 
