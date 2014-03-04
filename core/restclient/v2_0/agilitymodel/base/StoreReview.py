from core.restclient.v2_0.agilitymodel.base.Asset import AssetBase

class StoreReviewBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, userName=None, rating=None, title=None, createdOn=None, updatedOn=None, userId=None, comment=None, productId=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'userName': {'type': 'string', 'name': 'userName', 'minOccurs': '0', 'native': True}, 'rating': {'type': 'int', 'name': 'rating', 'minOccurs': '0', 'native': True}, 'updatedOn': {'type': 'date', 'name': 'updatedOn', 'minOccurs': '0', 'native': True}, 'createdOn': {'type': 'date', 'name': 'createdOn', 'minOccurs': '0', 'native': True}, 'title': {'type': 'string', 'name': 'title', 'minOccurs': '0', 'native': True}, 'userId': {'type': 'int', 'name': 'userId', 'minOccurs': '0', 'native': True}, 'comment': {'type': 'string', 'name': 'comment', 'minOccurs': '0', 'native': True}, 'productId': {'type': 'int', 'name': 'productId', 'minOccurs': '0', 'native': True}})
        self.userName = userName
        self.rating = rating
        self.title = title
        self.createdOn = createdOn
        self.updatedOn = updatedOn
        self.userId = userId
        self.comment = comment
        self.productId = productId 
