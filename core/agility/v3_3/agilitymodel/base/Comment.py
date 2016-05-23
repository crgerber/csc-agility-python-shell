from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class CommentBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, user=None, comment=None, createdon=None, updatedon=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'user': {'name': 'user', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'comment': {'name': 'comment', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'createdOn': {'name': 'createdon', 'minOccurs': '0', 'native': True, 'type': 'date'}, 'updatedOn': {'name': 'updatedon', 'minOccurs': '0', 'native': True, 'type': 'date'}})
        self.user = user
        self.comment = comment
        self.createdon = createdon
        self.updatedon = updatedon 
